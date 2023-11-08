import os
import shutil
import requests
import argparse

from aoc_utils import get_puzzle_data
from file_utils import mkdirs, touch, render_template


def create_aoc_project(destination_directory: str, day: int, year: int, delete: bool = False):
    project_name = "day" + str(day)
    destination_directory = destination_directory + "/" + project_name

    if os.path.exists(destination_directory):
        if delete:
            shutil.rmtree(destination_directory)

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    mkdirs(destination_directory, ["tests", "src"])

    touch(destination_directory + '/src', ["__init__.py"])
    touch(destination_directory + '/tests', ["__init__.py"])
    touch(destination_directory, ["puzzle_data_example.txt"])

    shutil.copy("./templates/test.sh", destination_directory)
    shutil.copy("./templates/test_pytest.py", destination_directory + "/tests")

    render_template("./templates/pyproject.toml", destination_directory, [["%name%", f"\"day{day}\""]])
    render_template("./templates/day.py", destination_directory + "/src", [["%day%", f"day{day}"]])

    os.rename(f"{destination_directory}/src/day.py", f"{destination_directory}/src/day{day}.py")

    puzzle_data = get_puzzle_data(year=year, day=1)

    with open(f"{destination_directory}/puzzle_data.txt", 'w') as file:
        file.write(puzzle_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create an AoC project')
    parser.add_argument('--day', type=int, help='The day to create a project for', required=True)
    parser.add_argument('--delete', action='store_true', help='Delete the project if it exists', default=False)
    parser.add_argument('--destination', type=str, help='The destination directory', required=True)
    parser.add_argument('--year', type=int, help='The year to create a project for', default=2022)
    args = parser.parse_args()

    match args.destination[0]:
        case '.':
            destination = os.path.abspath(args.destination)
        case '~':
            destination = os.path.expanduser(args.destination)
        case _:
            destination = args.destination

    create_aoc_project(destination, args.day, year=args.year, delete=args.delete)
