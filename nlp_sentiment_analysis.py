
import os
import csv
import codecs
import re
from string import punctuation

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'GCP_NLP_Credentials.json'

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# Sentiment Analysis
text = strip_punctuation("Red Cross is great!")
document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

sentiment = client.analyze_sentiment(document=document).document_sentiment

print(sentiment.score)
