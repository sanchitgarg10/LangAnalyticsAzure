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

# Request body for Sentiment Analysis
sentiment_analysis_body = {
    "kind": "SentimentAnalysis",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "language": "en",
                "text": "I have no words to describe the film, yikes"
            }
        ]
    }
}

# Make the POST request
response = requests.post(endpoint, headers=headers, json=sentiment_analysis_body)

# Check if the request was successful
if response.status_code == 200:
    response_json = response.json()
    print("Sentiment Analysis Results:")
    if "results" in response_json and "documents" in response_json["results"]:
        for document in response_json["results"]["documents"]:
            print(f"Document ID: {document['id']}")
            print(f"Document Sentiment: {document.get('sentiment', 'Unknown')}")
            for sentence in document.get("sentences", []):
                print(f"\tSentence: {sentence['text']}")
                print(f"\tSentence Sentiment: {sentence['sentiment']}")
    else:
        print("No results or documents found in the response.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
