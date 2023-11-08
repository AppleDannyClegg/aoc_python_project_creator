# Advent of Code project creator for Python

## Creates a project folder for the current year and day

### Usage:

```
python main.py --day 10 --year 2021 --destination "~/projects/git/day10" --delete  
```

### Options:

``` options:
  -h, --help            show this help message and exit
  --day DAY             The day to create a project for
  --delete              Delete the project if it exists
  --destination DESTINATION
                        The destination directory
  --year YEAR           The year to create a project for
```

### Requirements:

- Python 3.12
- [Poetry](https://python-poetry.org/docs/#installation)
- Need to set AOC_SESSION environment variable to your session cookie from the [Advent of Code](https://adventofcode.com/) website. You can find this in your browser's dev tools
  under the Application tab. It's called `session` and is under the Cookies section.
