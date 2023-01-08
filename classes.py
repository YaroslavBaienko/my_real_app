import json
import sqlite3
import requests
import random
from bs4 import BeautifulSoup
import os
import pathlib
from pathlib import Path


class Listinizer:
    def __init__(self, volume: int, rng: tuple, result=[]):
        self.volume = volume
        self.rng = rng
        self.result = result

    def get_list(self):
        dir_path = pathlib.Path.cwd()
        path = Path(dir_path, "data", "result.json")
        for item in range(self.volume):
            self.result.append(random.randint(*self.rng))
            with open(path, 'w') as file:
                json.dump(self.result, file)
                file.close()
        return self.result

    def reduced(self):
        dir_path = pathlib.Path.cwd()
        path = Path(dir_path, "data", "result.json")
        with open(path, "r") as file:
            self.res = json.load(file)
            for number, item in enumerate(self.res):
                self.res[number] = item // 2
        return self.res