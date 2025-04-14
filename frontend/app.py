import streamlit as st
import requests

API_URL = "http://127.0.0.1:6000/process-query"

st.set_page_config(page_title="Ticket Query App", layout="centered")
st.title("🎫 Ticket Query System")
st.write("Enter your query to fetch tickets from the database.")

query = st.text_input("🔍 Enter your query:", placeholder="E.g., Show high priority tickets assigned to John")

if st.button("Search"):
    if not query.strip():
        st.warning("Please enter a query before searching.")
    else:
        st.info("🔄 Fetching tickets... Please wait.")
        try:
            response = requests.post(API_URL, json={"query": query})
            
            if response.status_code == 200:
                data = response.json()
                tickets = data.get("tickets", [])
                
                if tickets:
                    st.success("✅ Tickets retrieved successfully!")
                    st.write("### 🎟️ Filtered Tickets:")
                    for ticket in tickets:
                        st.write(f"**Ticket ID:** {ticket[0]}")
                        st.write(f"**Description:** {ticket[1]}")
                        st.write(f"**Created On:** {ticket[2]}")
                        st.write(f"**Priority:** {ticket[3]}")
                        st.write(f"**Type:** {ticket[4]}")
                        st.write(f"**Assignee:** {ticket[5]}")
                        st.markdown("---")
                else:
                    st.warning("⚠️ No tickets found matching your query.")
            else:
                st.error(f"❌ Error {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"🚨 Connection error: {e}")