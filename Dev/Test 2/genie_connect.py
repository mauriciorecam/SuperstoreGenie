import requests
import os
from dotenv import load_dotenv

# Load token from .env
load_dotenv()
TOKEN = os.getenv("DATABRICKS_TOKEN")

# Constants
BASE_URL = "https://dbc-ff1901e9-f7d0.cloud.databricks.com"
ROOM_ID = "01f03f3cedd41b739f2426b8dcb37719"  # from your Genie space link
ORG_ID = "7214119327730999"  # from your Genie space link

# Conversation API endpoint
API_URL = f"{BASE_URL}/genie/api/o/{ORG_ID}/conversations"



# Headers with Databricks Token
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Example payload to start a new conversation
data = {
    "messages": [{"role": "user", "content": "Hello Genie, can you summarize my workspace data?"}],
    "room_id": ROOM_ID
}

# Send request
response = requests.post(API_URL, headers=headers, json=data)

# Show result
if response.ok:
    print("✅ Response:")
    print(response.json())
else:
    print("❌ Error:")
    print(response.status_code, response.text)
