import gradio as gr
import requests
from io import BytesIO
from PIL import Image

API_ENDPOINT = "http://localhost:8000/generate"

def generate_image_via_api(
    prompt: str,
    height: int,
    width: int,
    guidance_scale: float,
    num_inference_steps: int,
    max_sequence_length: int,
    seed: int
):
    """
    This function sends a request to the FastAPI endpoint, gets the image as a streaming response,
    and returns a PIL image to Gradio.
    """
    payload = {
        "prompt": prompt,
        "height": height,
        "width": width,
        "guidance_scale": guidance_scale,
        "num_inference_steps": num_inference_steps,
        "max_sequence_length": max_sequence_length,
        "seed": seed
    }

    # POST request to the FastAPI service
    response = requests.post(API_ENDPOINT, json=payload, stream=True)
    response.raise_for_status()  # Raise an error if request failed

    # The response content is PNG bytes. We read them into a PIL image.
    image = Image.open(BytesIO(response.content))
    return image


def main():
    with gr.Blocks() as demo:
        gr.Markdown("## Flux LoRA Image Generator (via FastAPI)")

        with gr.Row():
            prompt = gr.Textbox(label="Prompt", value="A cat holding a sign that says hello world")
            height = gr.Slider(label="Height", minimum=256, maximum=2048, step=64, value=512)
            width = gr.Slider(label="Width", minimum=256, maximum=2048, step=64, value=512)

        with gr.Row():
            guidance_scale = gr.Slider(label="Guidance Scale", minimum=1.0, maximum=20.0, step=0.5, value=3.5)
            steps = gr.Slider(label="Inference Steps", minimum=1, maximum=150, step=1, value=50)
            max_seq_len = gr.Slider(label="Max Sequence Length", minimum=64, maximum=1024, step=64, value=512)
            seed = gr.Number(label="Seed", value=42)

        generate_btn = gr.Button("Generate Image")

        # An output image component
        output_image = gr.Image(label="Generated Image")

        # Define what happens on button click
        generate_btn.click(
            fn=generate_image_via_api,
            inputs=[prompt, height, width, guidance_scale, steps, max_seq_len, seed],
            outputs=output_image
        )

    return demo

if __name__ == "__main__":
    # Launch the Gradio interface
    demo_app = main()
    demo_app.launch(server_name="0.0.0.0", server_port=7890)
