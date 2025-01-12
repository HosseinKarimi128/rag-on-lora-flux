"""
Module for extracting named entities from a user prompt.
You can implement actual NER logic using spaCy or other libraries.
Below is a simple placeholder for demonstration.
"""

def extract_named_entities(prompt: str):
    # A naive rule-based approach for demonstration:
    recognized_entities = []

    # If the prompt contains the word 'cat', consider that an entity:
    if "cat" in prompt.lower():
        recognized_entities.append("cat")

    # Add more rules or real NER here...

    return recognized_entities
