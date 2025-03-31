from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nlu import extract_entities, classify_intent
from tickets_retriever import retrieve_tickets

app = FastAPI()

# Pydantic model for user queries
class QueryRequest(BaseModel):
    query: str

@app.post("/process-query")
def process_query(request: QueryRequest):
    """
    Process the user's query and return filtered tickets.
    """
    # Step 1: Extract entities and classify intent
    extracted_data = extract_entities(request.query)
    intent = classify_intent(request.query)

    if intent == "fetch tickets":
        # Step 2: Retrieve tickets based on extracted data
        tickets = retrieve_tickets(extracted_data)
        if tickets:
            return {"intent": intent, "tickets": tickets}
        else:
            raise HTTPException(status_code=404, detail="No tickets found")
    else:
        raise HTTPException(status_code=400, detail="Invalid intent")

# Run the FastAPI server with: uvicorn main:app --reload
