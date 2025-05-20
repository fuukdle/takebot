import os
import tweepy

# Read day count
with open("daycount.txt", "r") as f:
    day_count = int(f.read().strip())

# Twitter API credentials from environment variables
client = tweepy.Client(
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_KEY_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
)

tweet_text = f"Yukari Takeba — Day {day_count}"

response = client.create_tweet(text=tweet_text)

if response.data:
    print(f"Tweeted: {tweet_text}")
else:
    print("Failed to tweet:", response.errors)
    exit(1)

# Increment day count and save
with open("daycount.txt", "w") as f:
    f.write(str(day_count + 1))
