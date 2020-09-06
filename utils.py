"""
Core utilities
"""

# stdlib
import random
from datetime import datetime
from typing import Iterable

# library
from dateutil.tz import gettz


def now() -> datetime:
    """
    Returns current time in US East
    """
    return datetime.now(tz=gettz("America/New_York"))


def excluding_range(start: int, stop: int, exclude: Iterable[int]) -> int:
    """
    Similar to randrange but can exclude values
    """
    index = random.randrange(start, stop)
    while index in exclude:
        index = random.randrange(start, stop)
    return index
