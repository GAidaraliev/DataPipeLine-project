import json
import math
import os
import sys


def my_function(x, y):
    print("Result is: ", x + y)
    return x + y


def unused_func():
    pass


class myclass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print("Value:", self.value)


if __name__ == "__main__":
    result = my_function(5, 10)
    obj = myclass(result)
    obj.show()


def add_numbers(a: int, b: int) -> int:
    return a + b


print(add_numbers(5, 10))
print(add_numbers("5", 10))

my_list = ["apple", "banana", "cherry"]

# --- System and OS ---
import pathlib
import shutil

print("Current working dir:", os.getcwd())
print("Python executable:", sys.executable)
tmp_file = pathlib.Path("example.txt")
tmp_file.write_text("Hello, world!")
shutil.copy("example.txt", "example_copy.txt")

# --- Math and Numbers ---
import decimal
import fractions
import random
import statistics

print("Square root of 16:", math.sqrt(16))
print("Random number:", random.randint(1, 10))
print("Mean of [1,2,3]:", statistics.mean([1, 2, 3]))
print("Decimal sum:", decimal.Decimal("0.1") + decimal.Decimal("0.2"))
print("Fraction:", fractions.Fraction(3, 4))

# --- Dates and Times ---
import calendar
import datetime
import time

now = datetime.datetime.now()
print("Now:", now)
print("Unix timestamp:", time.time())
print("Calendar for December 2025:\n", calendar.month(2025, 12))

# --- File Formats ---
import configparser
import csv
import sqlite3

data = {"name": "Гали", "age": 30}
print("JSON dump:", json.dumps(data))

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Гали", 30])

config = configparser.ConfigParser()
config["DEFAULT"] = {"Server": "localhost", "Port": "8080"}
with open("config.ini", "w") as f:
    config.write(f)

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Гали')")
conn.commit()
print("SQLite rows:", cursor.execute("SELECT * FROM users").fetchall())

# --- Networking ---
import urllib.parse
import urllib.request

url = "https://httpbin.org/get"
params = urllib.parse.urlencode({"q": "python"})
with urllib.request.urlopen(f"{url}?{params}") as response:
    print("HTTP status:", response.status)

# --- Concurrency ---
import asyncio
import threading


def worker():
    print("Thread worker running")

thread = threading.Thread(target=worker)
thread.start()
thread.join()

async def async_task():
    print("Async task running")

asyncio.run(async_task())

# --- Utilities ---
import dataclasses
import functools
import itertools
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is a log message")

print("Combinations:", list(itertools.combinations([1, 2, 3], 2)))

@functools.lru_cache
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

print("Fibonacci(10):", fib(10))

@dataclasses.dataclass
class User:
    id: int
    name: str

user = User(1, "Гали")
print("Dataclass user:", user)
