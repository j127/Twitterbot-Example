import tweepy

# You need to put your Twitter settings in the settings.py file for this to work
from settings import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# The `api` object contains the methods that you need to interact with Twitter.
# Load a Python 3 terminal from this directory and do `from bot import api`.
# The `api` object can then be used in the terminal.
