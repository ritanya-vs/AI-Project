from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nlu import extract_entities
from tickets_retriever import retrieve_tickets

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/process-query")
def process_query(request: QueryRequest):
    
    extracted_data = extract_entities(request.query)

    filtered_data = {k: v for k, v in extracted_data.items() if v}

    tickets = retrieve_tickets(filtered_data)

    if tickets:
        return {"tickets": tickets}
    else:
        raise HTTPException(status_code=404, detail="No tickets found for the given filters")
