import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Load environment variables
token = os.getenv("GENIE_TOKEN")
workspace_url = "https://dbc-ff1901e9-f7d0.cloud.databricks.com"
org_id = "7214119327730999"
room_id = "01f03f3cedd41b739f2426b8dcb37719"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

# Sample question to Genie
data = {
    "messages": [
        {"role": "user", "content": "Show me the top 5 customers by revenue."}
    ]
}

# API Endpoint
url = f"{workspace_url}/api/2.0/genie/conversation?o={org_id}&room_id={room_id}"

# Send request
response = requests.post(url, headers=headers, json=data)

# Output response
print("Status Code:", response.status_code)
print("Response:", response.json())
