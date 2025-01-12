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

# Load the base model once at import time.
# In a production scenario, you might load it in a startup event for efficiency.


def generate_image(
    prompt: str,
    height: int,
    width: int,
    guidance_scale: float,
    num_inference_steps: int,
    max_sequence_length: int,
    seed: int
):
    pipe = load_base_model()
    # 1) Extract named entities from prompt
    entities = extract_named_entities(prompt)

    # 2) Retrieve relevant LoRA models for these entities
    lora_info = get_lora_models(entities)

    # 3) If we have relevant LoRAs, load them dynamically
    #    This example sets all adapter weights to 0.8, but you can use your own logic
    if lora_info:
        
        load_lora_weights(pipe, lora_info)
        adapter_names = [adapter_name for _, adapter_name in lora_info]
        adapter_weights = [0.4 for _ in adapter_names]
        set_lora_weights(pipe, adapter_names, adapter_weights)

    # 4) Run inference
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
    return image
