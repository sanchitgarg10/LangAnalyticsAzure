import requests
import json

import os

key = os.environ.get('AZURE_KEY')
endpoint = os.environ.get('AZURE_ENDPOINT')
# Headers
headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": key
}

# Request body
body = {
    "kind": "KeyPhraseExtraction",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "language": "en",
                "text": "Dr. Smith has a very modern medical office, and she has great staff."
            }
        ]
    }
}

# Make the POST request
response = requests.post(endpoint, headers=headers, json=body)

# Check if the request was successful
if response.status_code == 200:
    response_json = response.json()
    print("Key Phrases:")

    if "results" in response_json and "documents" in response_json["results"]:
        for document in response_json["results"]["documents"]:
            if "keyPhrases" in document:
                for phrase in document["keyPhrases"]:
                    print(phrase)
            else:
                print(f"No key phrases found in document {document.get('id', 'Unknown')}")
    else:
        print("No results or documents found in the response.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)