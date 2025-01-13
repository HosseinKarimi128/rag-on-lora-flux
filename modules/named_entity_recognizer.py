import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np
from .retrieval import ENTITY_TO_LORA
import json

from utils.logger import setup_logger
logger = setup_logger("app_logger", "logs/app.log")

# Load NLP model and embedding model once
nlp = spacy.load("en_core_web_sm")

def load_custom_patterns(patterns_file):
    """
    Load custom entity patterns from a JSON file and add them to the NLP pipeline.
    """
    try:
        with open(patterns_file, "r") as f:
            patterns = json.load(f)
        ruler = nlp.add_pipe("entity_ruler", before="ner")
        ruler.add_patterns(patterns)
        logger.info("Custom patterns loaded successfully from %s.", patterns_file)
    except Exception as e:
        logger.error("Error loading custom patterns: %s", e)

load_custom_patterns("custom_entity_patterns.json")

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    """
    Generate an embedding for the given text using a Sentence Transformer model.
    """
    logger.debug("Generating embedding for text: %s", text)
    embedding = embedding_model.encode([text], convert_to_tensor=True)
    logger.debug("Generated embedding: %s", embedding)
    return embedding

def find_closest_entities(detected_entities, entity_to_lora_keys):
    """
    Find the closest matching entities based on semantic similarity.
    """
    recognized_entities = []
    lora_key_embeddings = {key: get_embedding(key) for key in entity_to_lora_keys}
    
    for entity in detected_entities:
        logger.debug("Processing entity: %s", entity)
        entity_embedding = get_embedding(entity)
        # logger.debug("Entity embedding shape: %s", entity_embedding.cpu().numpy().shape)
        # logger.debug("LoRA key embedding shape for %s: %s", key, lora_key_embeddings[key].cpu().numpy().shape)
        similarities = {
            key: cosine_similarity(
                entity_embedding.cpu().numpy().reshape(1, -1), 
                lora_key_embeddings[key].cpu().numpy().reshape(1, -1)
            )[0][0]
            for key in lora_key_embeddings
        }
        # Find the key with the highest similarity
        best_match = max(similarities, key=similarities.get)
        logger.debug("Best match for entity '%s': %s with similarity %f", entity, best_match, similarities[best_match])
        if similarities[best_match] > 0.5:  # Adjust threshold as needed
            recognized_entities.append(best_match)
            logger.info("Recognized entity: %s", best_match)
        else:
            logger.warning("No suitable match found for entity: %s", entity)
    return recognized_entities

def extract_named_entities(prompt: str):
    """
    Extract named entities using spaCy and match them semantically with ENTITY_TO_LORA keys.
    """
    logger.info("Extracting named entities from prompt: %s", prompt)
    doc = nlp(prompt)
    detected_entities = [ent.text.lower() for ent in doc.ents]
    logger.info("Detected entities: %s", detected_entities)
    for ent in ENTITY_TO_LORA.keys():
        if ent in prompt.lower():
            detected_entities.append(ent)
    logger.info("Detected entities after manual adding: %s", detected_entities)
    recognized_entities = find_closest_entities(detected_entities, ENTITY_TO_LORA.keys())
    logger.info("Recognized entities: %s", recognized_entities)
    return recognized_entities
