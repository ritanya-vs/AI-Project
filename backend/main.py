from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nlu import classify_intent
from tickets_retriever import retrieve_tickets

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/process-query")
def process_query(request: QueryRequest):
    """
    Process user query and return filtered tickets.
    """
    intent = classify_intent(request.query)

    if "fetch" in intent:
        tickets = retrieve_tickets({"Ticket Subject": request.query})
        if tickets:
            return {"intent": intent, "tickets": tickets}
        else:
            raise HTTPException(status_code=404, detail="No tickets found")
    else:
        raise HTTPException(status_code=400, detail="Invalid intent")
