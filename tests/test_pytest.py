import os
import shutil
import sys

from aoc_create_day.aoc_utils import get_puzzle_data
from aoc_create_day.file_utils import mkdirs, touch, render_template
from aoc_create_day.main import create_aoc_project


def test_create_day1():
    create_aoc_project("./_aoc", day=1, year=2018, delete=True)
    assert os.path.exists("./_aoc/day1")
    assert os.path.exists("./_aoc/day1/tests")
    assert os.path.exists("./_aoc/day1/src")
    assert os.path.exists("./_aoc/day1/src/__init__.py")
    assert os.path.exists("./_aoc/day1/tests/__init__.py")
    assert os.path.exists("./_aoc/day1/puzzle_data_example.txt")
    assert os.path.exists("./_aoc/day1/src/day1.py")
    shutil.rmtree("./_aoc/")


def test_mkdirs():
    base_path = "./test_mkdirs"
    dirs = ["test1", "test2", "test3"]

    mkdirs(base_path, dirs)

    assert os.path.exists(f"{base_path}/{dirs[0]}")
    assert os.path.exists(f"{base_path}/{dirs[1]}")
    assert os.path.exists(f"{base_path}/{dirs[2]}")

    os.rmdir(f"{base_path}/{dirs[0]}")
    os.rmdir(f"{base_path}/{dirs[1]}")
    os.rmdir(f"{base_path}/{dirs[2]}")
    os.rmdir(base_path)


def test_touch():
    base_path = "./test_touch"
    files = ["test1.txt", "test2.txt", "test3.txt"]

    mkdirs(base_path, [""])

    touch(base_path, files)

    assert os.path.exists(f"{base_path}/{files[0]}")
    assert os.path.exists(f"{base_path}/{files[1]}")
    assert os.path.exists(f"{base_path}/{files[2]}")

    os.remove(f"{base_path}/{files[0]}")
    os.remove(f"{base_path}/{files[1]}")
    os.remove(f"{base_path}/{files[2]}")
    os.rmdir(base_path)


def test_render_template():
    os.makedirs(os.path.abspath("./test_render_template"))

    render_template("/templates/test.sh", os.path.abspath("./test_render_template"), [["%day%", "day1"]])

    assert os.path.exists(os.path.abspath("./test_render_template/test.sh"))
    os.remove(os.path.abspath("./test_render_template/test.sh"))
    os.rmdir(os.path.abspath("./test_render_template"))


def test_get_puzzle_data():
    puzzle_data = get_puzzle_data(year=2018, day=1)

    assert len(puzzle_data) > 0
