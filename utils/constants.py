PATTERNS = [
    {
        "label": "PERSON",
        "pattern": [{"LOWER": "shahab"}, {"LOWER": "hosseini"}]
    },
    {
        "label": "CLOTHING",
        "pattern": [{"LOWER": "kurdish"}, {"LOWER": "clothing"}]
    }
]



ENTITY_TO_LORA = {
    "cat": ("strangerzonehf/Flux-Sketch-Ep-LoRA", "Sketch"),
    "shahab hosseini": ("HoKa/shahab-hosseini", "Shahab Hosseini"),
    "kurdish clothing": ("HoKa/man-kurdish-clothing", "Kurdish clothing"),
    "imam reza holy shrine": ("HoKa/imam-reza-holy-shrine", "Imam Reza Shrine")
    # Add more entity-to-LoRA mappings as needed
}