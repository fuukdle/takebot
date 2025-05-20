import os
import tweepy

client = tweepy.Client(
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_KEY_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
)

response = client.create_tweet(text="Yukari Takeba")

if response.data:
    print("Tweeted successfully!")
else:
    print("Failed to tweet:", response.errors)
