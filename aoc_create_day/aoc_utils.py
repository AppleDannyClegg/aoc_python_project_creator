import os

import requests


def get_puzzle_data(year: int, day: int):
    fetch_url = f"https://adventofcode.com/{year}/day/{day}/input"

    session_cookie = os.environ.get("AOC_SESSION")

    if not session_cookie:
        raise Exception("AOC_SESSION environment variable not set")

    http_response = requests.get(fetch_url, cookies={"session": session_cookie})

    if http_response.status_code == 200:
        return http_response.text
