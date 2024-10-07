from collections.abc import Callable
from functools import wraps
from time import time
from typing import Any


def log(filename: str | None) -> Callable:
    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                time_1 = time()
                result = func(*args, **kwargs)
                time_2 = time()
            except Exception as exc:
                result = 'error'
                if filename:
                    with open(filename, 'a', encoding='UTF-8') as file:
                        file.write(f'{func.__name__} {result}: {exc}. Inputs {args}, {kwargs}')
                else:
                    print(f'{func.__name__} {result}: {exc}. Inputs {args}, {kwargs}')
            else:
                if filename:
                    with open(filename, 'a', encoding='UTF-8') as file:
                        file.write(f'{func.__name__} ok\n')
                        file.write(f'Time start: {time_1}. Time end {time_2}\n')
                        file.write(f'Result: {result}')
                else:
                    print(f'{func.__name__} ok')
                    print(f'Time start: {time_1}. Time end {time_2}')
                    print(f'Result: {result}')
            return result
        return wrapper
    return my_decorator
