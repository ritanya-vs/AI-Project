import streamlit as st
import requests

# URL for the FastAPI backend (running locally on port 8000)
API_URL = "http://127.0.0.1:8000/process-query"

def get_filtered_tickets(query):
    """
    Sends a request to the FastAPI backend and returns the filtered tickets.
    """
    st.write("Step 2: Sending request to FastAPI backend...")
    response = requests.post(API_URL, json={"query": query})
    
    st.write("Step 3: Response received from backend")
    if response.status_code == 200:
        st.write("Step 4: Successfully retrieved data")
        return response.json()
    else:
        st.write("Step 4: Error encountered in backend response")
        return {"error": response.text}

# Streamlit UI
st.title("Ticket Query Processor")
st.write("Step 1: Streamlit app started")

# User input for query
query = st.text_input("Enter your query:")

if query:
    st.write("Step 2: Query entered by user ->", query)
    result = get_filtered_tickets(query)
    
    if "tickets" in result:
        st.write("Step 5: Displaying filtered tickets")
        st.write(result["tickets"])
    else:
        st.write("Step 5: Error occurred")
        st.error(f"Error: {result['error']}")
