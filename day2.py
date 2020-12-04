#!/usr/bin/env python
import re
from collections import Counter
from dataclasses import dataclass

ADVENT_DAY = "day2"

@dataclass
class PassLine:
    lo: int
    hi: int
    letter: str
    password: str


pass_policy = re.compile("(\d*)-(\d*) ([a-z]): (.*)")

def parse_line(line):
    obj = pass_policy.match(line)
    return PassLine(
        lo=int(obj[1]),
        hi=int(obj[2]),
        letter=obj[3],
        password=obj[4]
    )

def valid_passline(line):
    # Part 1:
    #char_freqs = Counter(line.password)
    #return line.lo <= char_freqs[line.letter] <= line.hi

    # Part 2:
    idx_lo = line.lo - 1
    idx_hi = line.hi - 1
    chars = [char for char in line.password]

    lo_exists = chars[idx_lo] == line.letter
    hi_exists = chars[idx_hi] == line.letter
    return lo_exists ^ hi_exists
    

def advent():
    lines = []
    with open(f'./{ADVENT_DAY}_input') as infile:
        lines = list(infile.read().split("\n"))

    to_check = [parse_line(l) for l in lines]
    print(f"{len(to_check)} passwords to check")

    valid = [line for line in to_check if valid_passline(line)]
    print(f"{len(valid)} passwords match their policy")

    

if __name__ == "__main__":
    advent()