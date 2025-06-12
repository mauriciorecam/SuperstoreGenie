import requests

# Replace with your actual info
GENIE_API_BASE = "https://e2-demo-west.cloud.databricks.com/api/2.0/genie"
GENIE_API_TOKEN = "dapic019aeca9c1c81a5b489891c337e4476"

headers = {
    "Authorization": f"Bearer {GENIE_API_TOKEN}",
    "Content-Type": "application/json",
}

# 1. Test token and create a new conversation
def create_conversation():
    url = f"{GENIE_API_BASE}/conversations"
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        conversation_id = response.json()["conversation_id"]
        print("✅ Conversation created:", conversation_id)
        return conversation_id
    else:
        print("❌ Failed to create conversation:", response.text)
        return None

# 2. Send a test message to Genie
def send_message(conversation_id, message):
    url = f"{GENIE_API_BASE}/conversations/{conversation_id}/messages"
    data = {
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        reply = response.json()["messages"][0]["content"]
        print("✅ Genie reply:", reply)
    else:
        print("❌ Failed to send message:", response.text)

# Run tests
if __name__ == "__main__":
    conversation_id = create_conversation()
    if conversation_id:
        send_message(conversation_id, "Hello Genie, can you hear me?")
