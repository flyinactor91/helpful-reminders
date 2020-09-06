"""
Twitter API handling
"""

# stdlib
from os import environ
from typing import List

# library
import tweepy

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_keys(*keys) -> List[str]:
    return [environ.get(key) for key in keys]


auth = tweepy.OAuthHandler(*get_keys("API_KEY", "API_SECRET"))
auth.set_access_token(*get_keys("USER_KEY", "USER_SECRET"))

api = tweepy.API(
    auth,
    wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True,
)


def tweet(msg: str) -> tweepy.Status:
    """
    Publishes a tweet
    """
    return api.update_status(msg)
