from typing import Any

from src.decorators import log


def test_log_1(capsys: Any) -> None:
    @log(None)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\nResult: 3\n"


def test_log_error(capsys: Any) -> None:
    @log(None)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function("1", 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: can only concatenate str (not \"int\") to str. Inputs ('1', 2), {}\n"
