"""
Module for extracting named entities from a user prompt.
You can implement actual NER logic using spaCy or other libraries.
Below is a simple placeholder for demonstration.
"""
from .retrieval import ENTITY_TO_LORA

def extract_named_entities(prompt: str):
    # A naive rule-based approach for demonstration:
    recognized_entities = []
    for ent in ENTITY_TO_LORA.keys():
        if ent in prompt.lower(): recognized_entities.append(ent)

    return recognized_entities
