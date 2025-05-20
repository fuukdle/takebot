import tweepy
import os

auth = tweepy.OAuth1UserHandler(
    os.environ["API_KEY"],
    os.environ["API_KEY_SECRET"],
    os.environ["ACCESS_TOKEN"],
    os.environ["ACCESS_TOKEN_SECRET"]
)

api = tweepy.API(auth)
api.update_status("Yukari Takeba")
