"""
Tweets the incorrect day of the week...except Tuesday
"""

import utils
from tweet import tweet

DAYS = ("Mon", "🌮 Tues", "Wednes", "Thurs", "Fri", "Satur", "Sun")


def lambda_handler(*_) -> None:
    now = utils.now()
    if now.weekday() == 1:
        index = 1
    else:
        index = utils.excluding_range(0, 7, (now.weekday(), 1))
    tweet(f"Today is {DAYS[index]}day")


if __name__ == "__main__":
    lambda_handler()
