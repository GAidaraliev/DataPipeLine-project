import os, sys
import math, json


def my_function(x: int, y: int) -> int:
    print("Result is: ", x + y)
    return x + y


def unused_func() -> None:
    pass


class myclass:
    def __init__(self, value: int) -> None:
        self.value = value

    def show(self) -> None:
        print("Value:", self.value)
        return None


if __name__ == "__main__":
    result = my_function(5, 10)
    obj = myclass(result)
    obj.show()
