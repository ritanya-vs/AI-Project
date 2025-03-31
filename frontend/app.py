import streamlit as st
import requests

# URL for the FastAPI backend (running locally on port 8000)
API_URL = "http://127.0.0.1:8000/process-query"

def get_filtered_tickets(query):
    """
    Sends a request to the FastAPI backend and returns the filtered tickets.
    """
    response = requests.post(API_URL, json={"query": query})
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

# Streamlit UI
st.title("Ticket Query Processor")

# User input for query
query = st.text_input("Enter your query:")

if query:
    result = get_filtered_tickets(query)
    if "tickets" in result:
        st.write("Filtered Tickets:")
        st.write(result["tickets"])
    else:
        st.error(f"Error: {result['error']}")
