"""
Tweets a message about a holiday
"""

# stdlib
import datetime as dt
from calendar import monthrange
from typing import Optional

# library
from dateutil.easter import easter as _easter

# module
import utils
from tweet import tweet


def is_nth_day(date: dt.date, nth: int, weekday: int, month: int) -> bool:
    """Returns True if date is the nth day of the week in a given month

    Params read as nth day of month ex: first monday in July
    n < 0 is end-indexed ex: -1 = last
    nth: -5 - 4
    weekday 0 - 6 Mon - Sun
    month 1 - 12
    """
    if date.month != month:
        return False
    if date.weekday() != weekday:
        return False
    if nth < 0:
        day_from_end = monthrange(date.year, date.month)[1] - date.day
        return day_from_end // 7 == (abs(nth) - 1)
    return (date.day - 1) // 7 == nth


def presidents_day(date: dt.date) -> Optional[str]:
    """Third Monday in February"""
    if not is_nth_day(date, 2, 0, 2):
        return None
    return "Something about presidents"


def dst_starts(date: dt.date) -> Optional[str]:
    """Second Sunday in March"""
    if not is_nth_day(date, 1, 6, 3):
        return None
    return "Daylight savings. Make sure to turn your clock back"


def easter(date: dt.date) -> Optional[str]:
    """Usually April. Handled by dateutil"""
    if date != _easter(date.year):
        return None
    return "Easter"


def mothers_day(date: dt.date) -> Optional[str]:
    """Second Sunday in May"""
    if not is_nth_day(date, 1, 6, 5):
        return None
    return "Mother's Day"


def memorial_day(date: dt.date) -> Optional[str]:
    """Last Monday in May"""
    if not is_nth_day(date, -1, 0, 5):
        return None
    return "Happy Labor Day"


def fathers_day(date: dt.date) -> Optional[str]:
    """Third Sunday in June"""
    if not is_nth_day(date, 2, 6, 6):
        return None
    return "Father's Day"


def labor_day(date: dt.date) -> Optional[str]:
    """First Monday in September"""
    if not is_nth_day(date, 0, 0, 9):
        return None
    return "Happy Memorial Day. You can wear white again"


def dst_ends(date: dt.date) -> Optional[str]:
    """First Sunday in November"""
    if not is_nth_day(date, 0, 6, 11):
        return None
    return "Daylight savings ends. Make sure to add an hour"


def thanksgiving(date: dt.date) -> Optional[str]:
    """Fourth Thursday in November"""
    if not is_nth_day(date, 3, 3, 11):
        return None
    return "Thanksgiving"


STATIC_DATES = {
    (1, 1): "New Years",
    (1, 20): "MLK",
    (2, 14): "Valentine's",
    (2, 29): "Leap Year",
    (3, 17): "St. Patrick's",
    (5, 5): "Cinco do Mayo",
    (6, 19): "Juneteenth",
    (7, 4): "July 4",
    (10, 31): "Halloween",
    (11, 11): "Veteran's",
    (12, 25): "Xmas",
    (12, 31): "New Year's Eve",
}


HANDLED_DATES = (
    presidents_day,
    dst_starts,
    easter,
    mothers_day,
    memorial_day,
    fathers_day,
    labor_day,
    dst_ends,
    thanksgiving,
)


def lambda_handler(*_) -> None:
    now = utils.now().date()
    tweets = []
    try:
        tweets.append(STATIC_DATES[(now.month, now.day)])
    except KeyError:
        pass
    for handler in HANDLED_DATES:
        msg = handler(now)
        if msg is not None:
            tweets.append(msg)
    print(tweets)


if __name__ == "__main__":
    lambda_handler()
