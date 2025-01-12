import torch
from diffusers import FluxPipeline

def load_base_model():
    """
    Loads the base Flux model from the Hugging Face Hub.
    Enable model CPU offload to balance CPU/GPU memory usage.
    """
    pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
    pipe.enable_model_cpu_offload()
    return pipe
