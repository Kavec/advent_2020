#!/usr/bin/env python
import math
ADVENT_DAY = "day3"

SLED_MOVE_PATTERNS = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1)

]


def gen_move_sled(map_width, move_pattern):
    (plus_row, plus_col) = move_pattern
    
    def move_sled(r, c):
        c = (c + plus_col) % map_width
        r = r + plus_row
        return (r, c)
    
    return move_sled

def check_trees(slope, move_fn):
    height = len(slope)

    cur_row = 0
    cur_col = 0
    n_trees = 0
    while cur_row < height:
        (cur_row, cur_col) = move_fn(cur_row, cur_col)
        if height <= cur_row:
            break

        if slope[cur_row][cur_col] == "#":
            n_trees += 1
    
    return n_trees


def advent():
    lines = []
    with open(f'./{ADVENT_DAY}_input') as infile:
        lines = list(infile.read().split("\n"))

    slope = [
        [char for char in line]
        for line in lines
    ]
    width = len(slope[0])
    runs = []
    for pattern in SLED_MOVE_PATTERNS:
        move_fn = gen_move_sled(width, pattern)
        n_trees = check_trees(slope, move_fn)

        (down, right) = pattern
        print(f"Ran into {n_trees} trees moving down {down} and right {right}")
        runs.append(n_trees)

    
    print(f"Multiplied together: {math.prod(runs)}")

    


if __name__ == "__main__":
    advent()