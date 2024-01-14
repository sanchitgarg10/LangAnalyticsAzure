import os
import requests

# Read key and endpoint from environment variables
key = os.environ.get('AZURE_KEY')
endpoint = os.environ.get('AZURE_LANGUAGE_ENDPOINT')

# Verify that key and endpoint are retrieved successfully
if key is None or endpoint is None:
    print("Error: Azure key or endpoint environment variables not set.")
else:
    # Specify the API path for language detection
    #language_detection_path = '/text/analytics/v3.1/languages'
    #url = endpoint + language_detection_path
    #print("Endpoint URL:", url)

    # Define the request body
    language_detection_body = {
        "documents": [
            {"id": "1", "text": "Hello world"},
            {"id": "2", "text": "Bonjour tout le monde"}
        ]
    }

    # Set up the headers
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": key
    }

    # Make the POST request
    response = requests.post(endpoint, headers=headers, json=language_detection_body)

    # Check if the request was successful and print the response
    if response.status_code == 200:
        print("Language Detection Results:")
        print(response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
