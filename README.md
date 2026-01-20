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
