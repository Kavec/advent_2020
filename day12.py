#!/usr/bin/env python
ADVENT_DAY = ""

def advent():
    lines = []
    with open(f'./{ADVENT_DAY}_input') as infile:
        lines = list(infile.read().splitlines())


if __name__ == "__main__":
    advent()