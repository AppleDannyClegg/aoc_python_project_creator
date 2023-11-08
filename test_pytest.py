import os

from aoc_utils import get_puzzle_data
from file_utils import mkdirs, touch, render_template
from main import create_aoc_project


def test_create_day1():
    create_aoc_project("./aoc", day=1, year=2018, delete=True)
    assert os.path.exists("./aoc/day1")
    assert os.path.exists("./aoc/day1/tests")
    assert os.path.exists("./aoc/day1/src")
    assert os.path.exists("./aoc/day1/src/__init__.py")
    assert os.path.exists("./aoc/day1/tests/__init__.py")


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
    base_path = "./test_render_template"
    template_path = "./templates/pyproject.toml"
    output_directory = base_path
    search_replace = [["%name%", f"\"day1\""]]

    mkdirs(base_path, [""])

    render_template(template_path, output_directory, search_replace)

    assert os.path.exists(f"{base_path}/pyproject.toml")

    os.remove(f"{base_path}/pyproject.toml")
    os.rmdir(base_path)


# create test for get_puzzle_data

def test_get_puzzle_data():
    puzzle_data = get_puzzle_data(year=2018, day=1)

    assert len(puzzle_data) > 0
