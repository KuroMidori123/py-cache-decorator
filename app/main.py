from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps
    def inner(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        elif key not in cache_dict:
            res = func(*args, **kwargs)
            cache_dict[key] = res
            print("Calculating new result")
            return res
    return inner
