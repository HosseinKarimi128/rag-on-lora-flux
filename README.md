# Retrieval LoRA Flux Image Generator

## Overview
Retrieval LoRA Flux Image Generator is an advanced image generation system leveraging LoRA (Low-Rank Adaptation) models for enhanced image synthesis. The system utilizes FastAPI for backend services and Gradio for an interactive user interface, allowing users to generate images based on text prompts while dynamically integrating relevant LoRA weights.

## Features
- **FastAPI-based Backend**: Provides an API endpoint for generating images based on text prompts.
- **Gradio UI**: A user-friendly web interface for interacting with the model.
- **Named Entity Recognition (NER)**: Extracts entities from prompts to enhance image generation with contextually relevant LoRA models.
- **Dynamic LoRA Weighting**: Selectively loads and applies LoRA weights based on recognized entities.
- **Torch-based Inference**: Uses Hugging Face's Diffusers library for efficient image synthesis.
- **Logging**: Integrated logging for monitoring and debugging.

## Installation
### Prerequisites
- Python 3.8+
- pip
- GPU recommended for faster inference (CUDA-enabled)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/retrieval-lora-flux-image-generator.git
   cd retrieval-lora-flux-image-generator
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Ensure required NLP models are downloaded:
   ```sh
   python -m spacy download en_core_web_sm
   ```
4. Start the FastAPI server:
   ```sh
   python -m app.main
   ```
5. Launch the Gradio interface:
   ```sh
   python gradio_app.py
   ```

## Usage
### API Usage
The FastAPI backend exposes an endpoint to generate images:
- **Endpoint**: `POST /generate`
- **Request Body (JSON)**:
  ```json
  {
    "prompt": "A cat holding a sign that says hello world",
    "height": 512,
    "width": 512,
    "guidance_scale": 3.5,
    "num_inference_steps": 50,
    "max_sequence_length": 512,
    "seed": 42
  }
  ```
- **Response**: Returns a PNG image stream.

### Gradio Interface
1. Open `http://localhost:7890` in your browser after running `gradio_app.py`.
2. Enter a prompt and adjust parameters as needed.
3. Click "Generate Image" to receive the generated image.

## Project Structure
```
retrieval-lora-flux-image-generator/
│── app/
│   ├── main.py          # FastAPI application
│   ├── __init__.py
│── gradio_app.py       # Gradio UI
│── model/
│   ├── base_model.py    # Base model loader
│   ├── inference.py     # Image generation logic
│   ├── lora_manager.py  # LoRA weight management
│── modules/
│   ├── named_entity_recognizer.py  # Entity extraction
│   ├── retrieval.py    # Retrieves relevant LoRA models
│── pipeline/
│   ├── workflow.py     # Main workflow handler
│── utils/
│   ├── constants.py    # Predefined entities & LoRA mappings
│   ├── logger.py       # Logging setup
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

## Configuration
- The `utils/constants.py` file defines example named entities and their associated LoRA models. You can replace or expand this list with other concepts as needed.
- The project supports different categories, including **places, clothing, and people**.

## Customization
To modify recognized entities:
1. Update `utils/constants.py` to include new entities.
2. Adjust `modules/named_entity_recognizer.py` to recognize them.
3. Add corresponding LoRA model references in `ENTITY_TO_LORA`.

## Troubleshooting
- **FastAPI server not starting?** Ensure `uvicorn` is installed and run `python -m app.main`.
- **Gradio interface not displaying?** Check `gradio_app.py` logs for errors.
- **Incorrect entity recognition?** Validate `spacy` model installation (`python -m spacy download en_core_web_sm`).
- **CUDA issues?** Ensure you have an appropriate PyTorch version for your GPU.

## License
GNU GENERAL PUBLIC LICENSE. Feel free to modify and distribute.

## Contributing
Pull requests are welcome! Ensure your changes are well-documented and tested before submitting.

## Acknowledgments
- **Hugging Face Diffusers** for model support.
- **spaCy** for entity recognition.
- **Gradio** for the interactive UI.
- Example entities (Iranian concepts) are for demonstration purposes; users can modify them as needed.

---

