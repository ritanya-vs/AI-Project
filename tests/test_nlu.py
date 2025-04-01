import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))

from nlu import extract_entities, classify_intent

def test_extract_entities():
    query = "Show me all urgent tickets assigned to John in the last week"
    expected = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }
    result = extract_entities(query)
    print("Extract Entities Test:", "PASSED" if result == expected else f"FAILED (Got {result})")

def test_classify_intent():
    query = "Show me all urgent tickets assigned to John"
    result = classify_intent(query)
    print("Classify Intent Test:", "PASSED" if result == "fetch tickets" else f"FAILED (Got {result})")

# Run tests
if __name__ == "__main__":
    test_extract_entities()
    test_classify_intent()
