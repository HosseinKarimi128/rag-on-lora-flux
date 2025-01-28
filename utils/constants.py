import spacy
nlp = spacy.load("en_core_web_sm")

place_entities = [
    "tomb of cyrus",
    "bam citadel",
    "arg of karim khan",
    "Shahzadeh Mahan Historical Garden",
    "Bisotun",
    "Persepolis",
    "Imam Reza Holy Shrine",
    "Si-o-Se Pol Bridge",
    "Bostan vault",
    "Alamut Castle",
    "Golestan Palace",
    "Naqshe Jahan Square",
    "Mount Damavand",
    "Milad Tower",
    "Hafez Tomb",
    "Azadi Tower",
    "Naqshe Rostam",
    "Lut Desert",
    "Darband",
    "Chahkooh Canyon"]

clothing_entities = [
    "kurdish clothes",
    "woman kurdish clothes", 
    "Man Northern Iranian clothes", 
    "Woman Northern Iranian clothes", 
    "man turkish clothes", 
    "Woman turkish clothes"]

person_entities = [
    "Ahmad Mehranfar",
    "Ali Nasirian",
    "Alireza Khamseh",
    "Amin Hayai",
    "Amin Zendegani",
    "Amir Aghaei",
    "Amir Hossein Arman",
    "Amir Hossein Rostami",
    "Amir Jadidi",
    "Amir Jafari",
    "Ashkan Khatibi",
    "Bahram Radan",
    "Bahram Afshari",
    "Farhad Aslani",
    "Hadi Kazemi",
    # "Hamed Behdad",
    "Hamid Goudarzi",
    "Hootan Shakiba",
    "Houman Seyyedi",
    "Javad Ezati",
    "Mehran Modiri",
    "MohammadReza Foroutan",
    "Mohammad Reza Golzar",
    "Mohsen Tanabandeh",
    "Navid Mohammadzadeh",
    # "Parsa Pirouzfar",
    # "Parviz Parastui",
    "Payman Maadi",
    "Pejman Bazeghi",
    "Rambod Javan",
    "Reza Attaran",
    "Saeed Aghakhani",
    "Sam Derakhshani",
    'Shahab Hosseini'
]
# Generate the ENTITY_TO_LORA dictionary for all provided values
all_entities = place_entities + clothing_entities + person_entities
print(all_entities)
# Generate the dictionary
ENTITY_TO_LORA = {
    entity.lower().replace(" ", "-"): (f"HoKa/{entity.lower().replace(' ', '-')}", entity)
    for entity in all_entities
}
# Function to classify and generate patterns
PATTERNS = []

# Process each entity
for entity in all_entities:
    doc = nlp(entity)  # Process the entity through spaCy
    for ent in doc.ents:  # Check if spaCy recognizes an entity
        # Create a pattern dynamically
        pattern = [{"LOWER": word.lower()} for word in entity.split()]
        if entity in place_entities:
            label = "PLACE"
        elif entity in clothing_entities:
            label = "CLOTHING"
        elif entity in person_entities:
            label = "PERSON"
        PATTERNS.append({"label": label, "pattern": pattern})


print(PATTERNS[0:3])