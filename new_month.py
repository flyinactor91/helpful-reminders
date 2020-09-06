"""
Tweets the incorrect month name
"""

import utils
from tweet import tweet

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "🎃 Spoop",
    "November",
    "December",
)


def lambda_handler(*_) -> None:
    now = utils.now()
    if now.month == 10:
        index = 10
    else:
        index = utils.excluding_range(1, 13, (now.month, 10))
    tweet(f"Another month down. Welcome to {MONTHS[index]}")


if __name__ == "__main__":
    lambda_handler()
