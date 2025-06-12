import streamlit as st
import requests

# -- Configuration --
GENIE_API_BASE = "https://e2-demo-west.cloud.databricks.com/api/2.0/genie"
GENIE_API_TOKEN = st.secrets["GENIE_API_TOKEN"]
CONVERSATION_ID = "01f018b6e77b1d24b2b3c6d21b3f5d0c"

headers = {
    "Authorization": f"Bearer {GENIE_API_TOKEN}",
    "Content-Type": "application/json",
}

st.title("💬 Chat with Genie (Existing Conversation)")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
 
# User input
if prompt := st.chat_input("Ask something about your data..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send message to Genie
    data = {"messages": [{"role": "user", "content": prompt}]}
    response = requests.post(
        f"{GENIE_API_BASE}/conversations/{CONVERSATION_ID}/messages",
        headers=headers,
        json=data,
    )

    if response.status_code == 200:
        reply = response.json()["messages"][0]["content"]
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
    else:
        st.error("Genie API returned an error.")
