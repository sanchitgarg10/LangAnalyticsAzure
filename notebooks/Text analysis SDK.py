# Import required libraries
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Retrieve endpoint and key from environment variables
endpoint = os.environ.get('AZURE_ENDPOINT2')
key = os.environ.get('AZURE_KEY')

# Create a Text Analytics client
credential = AzureKeyCredential(key)
ai_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Sample text for analysis
text = ["The Eiffel Tower is an iconic landmark located in Paris, France. Built in 1889, it attracts millions of tourists each year. Visitors often say they are impressed by the breathtaking view of the city from the top. However, some have mentioned that the long queues can be quite frustrating. In recent news, the tower was illuminated in green to promote environmental awareness. This event was widely covered and shared across social media platforms, highlighting the importance of sustainable practices. The Eiffel Tower, besides being a symbol of architectural beauty, has become a beacon for eco-friendly initiatives."
]

# Language Detection
response = ai_client.detect_language(documents=text)
print('\nLanguage:', response[0].primary_language.name)

# Sentiment Analysis
response = ai_client.analyze_sentiment(documents=text)
print('\nSentiment:', response[0].sentiment)

# Key Phrase Extraction
response = ai_client.extract_key_phrases(documents=text)
if len(response[0].key_phrases) > 0:
    print('\nKey Phrases:')
    for phrase in response[0].key_phrases:
        print('\t', phrase)

# Entity Recognition
response = ai_client.recognize_entities(documents=text)
if len(response[0].entities) > 0:
    print('\nEntities:')
    for entity in response[0].entities:
        print('\t', entity.text, '(', entity.category, ')')

# Linked Entity Recognition
response = ai_client.recognize_linked_entities(documents=text)
if len(response[0].entities) > 0:
    print('\nLinked Entities:')
    for linked_entity in response[0].entities:
        print('\t', linked_entity.name, '(', linked_entity.url, ')')
