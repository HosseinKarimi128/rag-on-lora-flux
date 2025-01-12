# app/main.py

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional
import uvicorn
from io import BytesIO
from pipeline.workflow import generate_image


from utils.logger import setup_logger
logger = setup_logger("app_logger", "logs/app.log")

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
    Endpoint that generates an image based on the given prompt
    and returns it directly as a PNG image stream.
    """
    logger.info("Received request to generate image with prompt: %s", req.prompt)
    
    try:
        image = generate_image(
            prompt=req.prompt,
            height=req.height,
            width=req.width,
            guidance_scale=req.guidance_scale,
            num_inference_steps=req.num_inference_steps,
            max_sequence_length=req.max_sequence_length,
            seed=req.seed
        )
        
        logger.info("Image generated successfully.")
        
        # Convert the PIL image to a buffer
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        # Return the buffer as a streaming response with image/png MIME type
        return StreamingResponse(buffer, media_type="image/png")
    
    except Exception as e:
        logger.error("Error generating image: %s", e)
        return {"error": "Image generation failed"}, 500

if __name__ == "__main__":
    logger.info("Starting FastAPI application.")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
