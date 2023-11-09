import os
import shutil
import argparse

import os.path

from file_utils import mkdirs, render_template, touch
from aoc_utils import get_puzzle_data


def create_aoc_project(destination_directory: str, day: int, year: int, delete: bool = False):
    match destination_directory[0]:
        case '.':
            destination_directory = os.path.abspath(destination_directory)
        case '~':
            destination_directory = os.path.expanduser(destination_directory)
        case _:
            pass

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

    render_template("/templates/test_pytest.py", destination_directory + "/tests", [])
    render_template("/templates/test.sh", destination_directory, [])
    render_template("/templates/pyproject.toml", destination_directory, [["%name%", f"\"day{day}\""]])
    render_template("/templates/day.py", destination_directory + f"/src/day{day}.py", [["%day%", f"day{day}"]])

    puzzle_data = get_puzzle_data(year=year, day=1)

    with open(f"{destination_directory}/puzzle_data.txt", 'w') as file:
        file.write(puzzle_data)


if __name__ == "__main__":
    # load_dotenv()

    parser = argparse.ArgumentParser(description='Create an AoC project')
    parser.add_argument('--day', type=int, help='The day to create a project for', required=True)
    parser.add_argument('--delete', action='store_true', help='Delete the project if it exists', default=False)
    parser.add_argument('--destination', type=str, help='The destination directory', required=True)
    parser.add_argument('--year', type=int, help='The year to create a project for', default=2022)
    args = parser.parse_args()

    # rewrite the following

    create_aoc_project(args.destination, args.day, year=args.year, delete=args.delete)
