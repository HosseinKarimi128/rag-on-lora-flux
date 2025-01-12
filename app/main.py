from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

# We import our main workflow function
from pipeline.workflow import generate_image

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    height: Optional[int] = 512
    width: Optional[int] = 512
    guidance_scale: Optional[float] = 3.5
    num_inference_steps: Optional[int] = 50
    max_sequence_length: Optional[int] = 512
    seed: Optional[int] = 42


@app.post("/generate")
def generate_prompted_image(req: PromptRequest):
    """
    Endpoint that generates an image based on the given prompt.
    Dynamically loads LoRA weights depending on named entities extracted from the prompt.
    """
    image = generate_image(
        prompt=req.prompt,
        height=req.height,
        width=req.width,
        guidance_scale=req.guidance_scale,
        num_inference_steps=req.num_inference_steps,
        max_sequence_length=req.max_sequence_length,
        seed=req.seed
    )

    # For a real application, you might return the image in base64 or store it and return a URL.
    # Here, we'll just return a simple JSON indicating success.
    return {"message": "Image generation successful."}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
