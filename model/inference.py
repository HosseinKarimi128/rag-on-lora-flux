import torch

def run_inference(pipe, prompt, height, width, guidance_scale, num_inference_steps, max_sequence_length, seed):
    """
    Run the actual image generation inference, returning a PIL image object.
    """
    generator = torch.Generator("cpu").manual_seed(seed)

    image = pipe(
        prompt,
        height=height,
        width=width,
        guidance_scale=guidance_scale,
        num_inference_steps=num_inference_steps,
        max_sequence_length=max_sequence_length,
        generator=generator
    ).images[0]

    return image
