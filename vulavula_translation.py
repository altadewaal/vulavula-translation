VULAVULA_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMThmNThiMDAtZjViZC00NzE4LTg5NGItMGE2MTNmMjA0OWE2Iiwia2V5Y2hhaW5faWQiOiIwY2NlNzdlZS01NjEyLTQ5MjEtODY5NC1mMTBlNjYyNGM3NDAiLCJwcm9qZWN0X2lkIjoiNWRmNDcyM2QtNTRiYi00ZGIzLWIxOGUtMDk4ZTBkMDNiNzBkIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDctMjFUMTk6Mjk6NDAuMTQzNzgyIn0.9lBDbBAHCL81eqmrNDGW_WqoY1H4gH608-291CglyhA"
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