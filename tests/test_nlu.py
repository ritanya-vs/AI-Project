from nlu_module import extract_entities, classify_intent

def test_extract_entities():
    query = "Show me all urgent tickets assigned to John in the last week"
    expected = {
        "priority": "high",
        "assignee": "John",
        "time_range": "last week"
    }
    assert extract_entities(query) == expected

def test_classify_intent():
    query = "Show me all urgent tickets assigned to John"
    assert classify_intent(query) == "fetch tickets"
