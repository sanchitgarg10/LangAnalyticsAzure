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

# Request body for Entity Linking
entity_linking_body = {
    "kind": "EntityLinking",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "language": "en",
                "text": "Rahul Dravid is a great wicketkeeper in cricket"
            }
        ]
    }
}

# Make the POST request
response = requests.post(endpoint, headers=headers, json=entity_linking_body)

# Check if the request was successful
if response.status_code == 200:
    response_json = response.json()
    print("Entity Linking Results:")
    
    if "results" in response_json and "documents" in response_json["results"]:
        for document in response_json["results"]["documents"]:
            print(f"Document ID: {document['id']}")
            for entity in document.get("entities", []):
                print(f"\tEntity Name: {entity['name']}")
                print(f"\tWikipedia URL: {entity.get('url', 'No URL')}")
                print(f"\tConfidence Score: {entity['matches'][0].get('confidenceScore', 'N/A')}")
    else:
        print("No results or documents found in the response.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)