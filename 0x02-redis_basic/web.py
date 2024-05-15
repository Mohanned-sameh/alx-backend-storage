#!/usr/bin/env python3
"""
Caching request module
"""
from typing import Callable
import redis
import requests


def cache_url(redis: redis.client.Redis, url: str) -> str:
    """
    Cache the result of the request
    """
    key = f"result:{url}"
    redis.set(key, get_page(url))
    redis.expire(key, 10)
    return redis.get(key).decode("utf-8")


def get_page(url: str) -> str:
    """
    Get the content of the page
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    r = redis.Redis()
    get_page = cache_url(
        r, "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.co.uk"
    )
    print(get_page)
