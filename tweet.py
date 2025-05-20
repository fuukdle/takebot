import os
import requests

BEARER_TOKEN = os.environ["BEARER_TOKEN"]

tweet_text = "Yukari Takeba"

url = "https://api.twitter.com/2/tweets"

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "text": tweet_text
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 201:
    print("Tweeted successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
    response.raise_for_status()
