from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str | None) -> Callable:
    """Декоратор для логирования вызовов функций"""

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                result = "error"
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} {result}: {exc}. Inputs {args}, {kwargs}")
                else:
                    print(f"{func.__name__} {result}: {exc}. Inputs {args}, {kwargs}")
            else:
                if filename:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok\n")
                        file.write(f"Result: {result}")
                else:
                    print(f"{func.__name__} ok")
                    print(f"Result: {result}")
            return result

        return wrapper

    return my_decorator
