"""
This module orchestrates the entire workflow:
  1) Named Entity Recognition
  2) Retrieval of relevant LoRA model references
  3) Dynamically loading LoRA weights
  4) Running inference with the combined model
"""

from modules.named_entity_recognizer import extract_named_entities
from modules.retrieval import get_lora_models
from model.base_model import load_base_model
from model.lora_manager import unload_lora_weights, load_lora_weights, set_lora_weights
from model.inference import run_inference
from utils.logger import setup_logger
logger = setup_logger("app_logger", "logs/app.log")

def generate_image(
    prompt: str,
    height: int,
    width: int,
    guidance_scale: float,
    num_inference_steps: int,
    max_sequence_length: int,
    seed: int
):
    logger.info("Starting image generation process.")
    logger.debug("Prompt: %s, Height: %d, Width: %d", prompt, height, width)

    pipe = load_base_model()
    logger.info("Base model loaded successfully.")

    # 1) Extract named entities from prompt
    entities = extract_named_entities(prompt)
    logger.debug("Extracted entities: %s", entities)

    # 2) Retrieve relevant LoRA models for these entities
    lora_info = get_lora_models(entities)
    logger.debug("Retrieved LoRA information: %s", lora_info)

    # 3) If we have relevant LoRAs, load them dynamically
    if lora_info:
        logger.info("Loading LoRA weights for entities.")
        load_lora_weights(pipe, lora_info)
        adapter_names = [adapter_name for _, adapter_name in lora_info]
        adapter_weights = [0.8 for _ in adapter_names]
        set_lora_weights(pipe, adapter_names, adapter_weights)
        logger.debug("Set LoRA weights: %s", adapter_weights)

    # 4) Run inference
    logger.info("Running inference.")
    image = run_inference(
        pipe=pipe,
        prompt=prompt,
        height=height,
        width=width,
        guidance_scale=guidance_scale,
        num_inference_steps=num_inference_steps,
        max_sequence_length=max_sequence_length,
        seed=seed
    )
    logger.info("Image generation completed successfully.")
    return image
