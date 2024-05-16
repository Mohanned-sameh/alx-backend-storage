#!/usr/bin/env python3
"""
Caching request module
"""
from functools import wraps
from typing import Callable
import requests
import redis

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    Count the number of requests
    """

    @wraps(method)
    def wrapper(url):
        """
        Wrapper function
        """
        r.incr(f"count:{url}")
        return method(url)

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Get the HTML content of a page
    """
    return requests.get(url).text
