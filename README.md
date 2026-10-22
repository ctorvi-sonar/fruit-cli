# Fruit CLI

A simple command-line tool that generates random fruits.

## Installation

```bash
uv pip install -e .
```

## Usage

Get one random fruit (default):

```bash
uv run main.py
```

Get a specific number of random fruits:

```bash
uv run main.py 5
```

View help:

```bash
uv run main.py --help
```

## Examples

```bash
$ uv run main.py
Apple

$ uv run main.py 3
Mango
Strawberry
Kiwi

$ uv run main.py 10
Banana
Cherry
Orange
Pineapple
Grape
Watermelon
Peach
Lime
Papaya
Blueberry
```

## Features

- Returns one random fruit by default
- Accepts a number argument to return multiple fruits
- Comprehensive list of 30 different fruits
- Proper error handling for invalid inputs
- Clean command-line interface with help documentation
- Case-insensitive substring filtering with `--filter`
- Sampling without duplicates with `--unique`
- Reproducible selections with `--seed`
- JSON arrays with `--format json`
- Listing the catalog with `--list` (optionally filtered)

```bash
uv run main.py 2 --filter apple --unique --seed 42 --format json
uv run main.py --list --filter berry
python -m unittest discover -v
```

Unique selections cannot exceed the number of matching fruits. Generation fails
when no fruits match; listing an empty result succeeds (JSON output is `[]`).
In list mode, count, seed, and unique options are ignored.

`issues/fruit_demo.py` contains intentional, harmless Sonar rule examples for
scanner testing. It is not imported by the CLI or included in the installed package.
