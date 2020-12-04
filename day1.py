#!/usr/bin/env python

from itertools import permutations

ADVENT_DAY = "day1"

def advent():
    numbers = []
    with open(f'./{ADVENT_DAY}_input') as infile:
        numbers = list(map(int, infile.read().split("\n")))

    # nee, pairs
    triples = [
        (a, b, c) for (a, b, c) in permutations(numbers, 3)
        if a + b + c == 2020
    ]

    nums = [a * b * c for (a, b, c) in triples]
    print(nums)



if __name__ == "__main__":
    advent()