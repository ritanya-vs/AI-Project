import spacy
import re

# Load spaCy English NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined mappings for entity extraction
PRIORITY_KEYWORDS = {
    "High": ["urgent", "critical", "top priority", "high"],
    "Medium": ["normal", "moderate", "medium"],
    "Low": ["low", "minor", "non-urgent"],
}

TIME_PATTERNS = {
    "today": r"today",
    "yesterday": r"yesterday",
    "last week": r"(last week|past week)",
    "last month": r"(last month|past month)",
}

TICKET_TYPES = ["Technical issue", "Billing inquiry", "Cancellation request", "Product inquiry", "Refund request"]
# ["bug", "feature request", "incident", "task", "change request"]

def extract_entities(query):
    doc = nlp(query)

    extracted_data = {"priority": None, "assignee": None, "time_range": None, "ticket_type": None}

    # Extract Named Entities (Assignee Name Detection)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            extracted_data["assignee"] = ent.text.capitalize()

    # Priority Extraction (Case-Insensitive Matching)
    query_lower = query.lower()
    for priority, synonyms in PRIORITY_KEYWORDS.items():
        if any(word in query_lower.split() for word in synonyms):
            extracted_data["priority"] = priority
            break

    # Time Range Extraction (Regex Matching)
    for time_key, pattern in TIME_PATTERNS.items():
        if re.search(pattern, query, re.IGNORECASE):
            extracted_data["time_range"] = time_key

    # Ticket Type Extraction
    for ticket_type in TICKET_TYPES:
        if ticket_type in query_lower:
            extracted_data["ticket_type"] = ticket_type.capitalize()
            break

    return extracted_data

# Example usage
if __name__ == "__main__":
    query = "Show me all urgent Technical issue tickets assigned to John"
    extracted_info = extract_entities(query)
    print("Extracted Information:", extracted_info)
