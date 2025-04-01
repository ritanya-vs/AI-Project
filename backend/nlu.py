import spacy
import re
from transformers import pipeline
from transformers import BartForConditionalGeneration, BartTokenizer
import torch

# Load fine-tuned model
MODEL_PATH = "fine_tuned_bart"
tokenizer = BartTokenizer.from_pretrained(MODEL_PATH)
model = BartForConditionalGeneration.from_pretrained(MODEL_PATH)

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Pretrained transformer for NLP-based classification (alternative to spaCy)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Predefined mappings for entity extraction
PRIORITY_KEYWORDS = {
    "high": ["urgent", "critical", "top priority"],
    "medium": ["normal", "moderate"],
    "low": ["low", "minor", "non-urgent"],
}

TIME_PATTERNS = {
    "today": r"today",
    "yesterday": r"yesterday",
    "last week": r"(last week|past week)",
    "last month": r"(last month|past month)",
}

def extract_entities(query):
    """
    Extracts priority, assignee, and time range from user query.
    """
    doc = nlp(query.lower())

    # Initialize extracted entities
    extracted_data = {"priority": None, "assignee": None, "time_range": None}

    # Step 1: Extract Named Entities (Assignee Name Detection)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            extracted_data["assignee"] = ent.text.capitalize()

    # Step 2: Priority Extraction (Rule-based Matching)
    for word in query.split():
        for priority, synonyms in PRIORITY_KEYWORDS.items():
            if word in synonyms or word == priority:
                extracted_data["priority"] = priority

    # Step 3: Time Range Extraction (Regex Matching)
    for time_key, pattern in TIME_PATTERNS.items():
        if re.search(pattern, query):
            extracted_data["time_range"] = time_key

    return extracted_data


def classify_intent(query):
    """
    Uses fine-tuned BART to classify ticket priority.
    """
    inputs = tokenizer(query, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    output = model.generate(**inputs)
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded_output  # Priority classification result


# Example usage
if __name__ == "__main__":
    query = "Show me all urgent tickets assigned to John in the last week"
    extracted_info = extract_entities(query)
    intent = classify_intent(query)

    print("Extracted Information:", extracted_info)
    print("Detected Intent:", intent)
