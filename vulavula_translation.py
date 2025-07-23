import os
from dotenv import load_dotenv

load_dotenv()
VULAVULA_TOKEN = os.getenv("VULAVULA_TOKEN")

# Endpoint URL
import requests
url = 'https://vulavula-services.lelapa.ai/api/v1/translate/process'

# Headers
headers = {
    'Content-Type': 'application/json',
    'X-CLIENT-TOKEN': VULAVULA_TOKEN # Replace '<INSERT_TOKEN>' with your actual client token
}

# Request body
data = {
  "input_text": "Hallo, hierdie is Afrikaans. Hoop jy geniet die vertaling!",
  "source_lang": "afr_Latn",
  "target_lang": "eng_Latn"
}

# Sending POST request
response = requests.post(url, headers=headers, json=data)

# Printing response
print(response.json())