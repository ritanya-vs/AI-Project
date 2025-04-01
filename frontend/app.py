import streamlit as st
import requests

# URL for the FastAPI backend (running locally on port 6000)
API_URL = "http://127.0.0.1:6000/process-query"

def get_filtered_tickets(query):
    """
    Sends a request to the FastAPI backend and returns the filtered tickets.
    """
    st.write("Step 2: Sending request to FastAPI backend...")
    
    # Send POST request with the user query
    try:
        response = requests.post(API_URL, json={"query": query})
    except requests.exceptions.RequestException as e:
        st.write("Step 4: Error encountered while sending request.")
        st.error(f"Request error: {e}")
        return {"error": str(e)}
    
    st.write("Step 3: Response received from backend")
    
    # Check for successful response
    if response.status_code == 200:
        st.write("Step 4: Successfully retrieved data")
        return response.json()  # Expecting the response to be a JSON object
    else:
        st.write("Step 4: Error encountered in backend response")
        st.error(f"Error {response.status_code}: {response.text}")
        return {"error": f"Error {response.status_code}: {response.text}"}

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
        st.write(result["tickets"])  # Show filtered tickets
    else:
        st.write("Step 5: Error occurred")
        st.error(f"Error: {result['error']}")
