from utils.logger import setup_logger
logger = setup_logger("app_logger", "logs/app.log")

"""
Module responsible for mapping recognized entities to relevant LoRA model references.
You can expand or replace this lookup logic with a real database or vector store retrieval.
"""

# Example: A dictionary that maps entity -> (LoRA repository path, suggested adapter name).
ENTITY_TO_LORA = {
    "cat": ("strangerzonehf/Flux-Sketch-Ep-LoRA", "Sketch"),
    "shahab hosseini": ("HoKa/shahab-hosseini", "Shahab Hosseini"),
    "kurdish clothing": ("HoKa/man-kurdish-clothing", "Kurdish clothing")
    # Add more entity-to-LoRA mappings as needed
}

def get_lora_models(entities):
    """
    Given a list of recognized entities, returns a list of tuples:
        [(lora_model_path, adapter_name), (lora_model_path, adapter_name), ...]
    """
    loras = []
    logger.info("Retrieving LoRA models for entities: %s", entities)
    for ent in entities:
        if ent in ENTITY_TO_LORA:
            loras.append(ENTITY_TO_LORA[ent])
            logger.debug("Found LoRA model for entity '%s': %s", ent, ENTITY_TO_LORA[ent])
        else:
            logger.warning("No LoRA model found for entity: %s", ent)
    logger.info("Retrieved LoRA models: %s", loras)
    return loras
