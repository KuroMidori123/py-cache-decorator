from typing import Callable


def cache(func: Callable) -> Callable:
    res_lst = {}

    def inner(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))
        if key in res_lst:
            print("Getting from cache")
            return res_lst[key]
        elif key not in res_lst:
            res = func(*args, **kwargs)
            res_lst[key] = res
            print("Calculating new result")
            return res
    return inner

