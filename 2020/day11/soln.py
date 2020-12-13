#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp

from collections import defaultdict
from functools import partial

# --- Soltuion ---

EMPTY = 'L'
OCCUP = '#'
FLOOR = '.'

def grid_size(grid):
    return (len(grid), len(grid[0]))

def count_rule(rule, grid, size, x, y):
    max_x, max_y = size
    neighbours = ""
    if x > 0:
        if y > 0:
            neighbours += rule(grid, x, y, -1, -1)
        if y < (max_y - 1):
            neighbours += rule(grid, x, y, -1, 1)
        neighbours += rule(grid, x, y, -1,  0)
    if x < (max_x - 1):
        if y > 0:
            neighbours += rule(grid, x, y, 1, -1)
        if y < (max_y - 1):
            neighbours += rule(grid, x, y, 1, 1)
        neighbours += rule(grid, x, y, 1, 0)
    if y > 0:
        neighbours += rule(grid, x, y, 0, -1)
    if y < (max_y - 1):
        neighbours += rule(grid, x, y, 0,  1)

    return neighbours.count(OCCUP)


def iterate(grid_in, rule, limit):
    occup = 0
    grid_out = []
    size = grid_size(grid_in)
    for i, row_in in enumerate(grid_in):
        row_out = ""
        for j, pos_in in enumerate(row_in):
            count = rule(grid_in, size, i, j)

            if pos_in == EMPTY:
                pos_out = OCCUP if count == 0 else EMPTY
            elif pos_in == OCCUP:
                pos_out = EMPTY if count >= limit else OCCUP
            else:
                pos_out = FLOOR
            if pos_out == OCCUP:
                occup += 1
            row_out += pos_out
        grid_out.append(row_out)
    return occup, grid_out

def execute(grid, rule, limit):
    curr_occup = -1
    prev_occup = -2
    while curr_occup != prev_occup:
        prev_occup = curr_occup
        curr_occup, grid = iterate(grid, rule, limit)
        # pp(grid)

    return curr_occup

def find_neighbour(grid, x, y, dx, dy):
    return grid[x+dx][y+dy]

def part1(grid):
    return execute(grid, partial(count_rule, find_neighbour), 4)

# def record_last(grid, record, start, delta):
#     last_seen = FLOOR
#
# def update_last(last, new):
#     return new if new != FLOOR else last
#
# def update(grid, record, pos, last):
#     return
#
# def do_diag(grid, size, record, start, dirn):
#     lazy_max = max(size[0], size[1])
#
#     inc_last = FLOOR
#     dec_last = FLOOR
#
#     for i in reversed(range(lazy_max)):
#         x_inc, y_inc = start[0] - i, start[1] - i
#         x_dec, y_dec = start[0] + i, start[1] + i
#
#         if x_inc >= 0 and y_inc >= 0:
#
#
#
# def pre_process_grid(grid, size):
#     max_x, max_y = size
#     record = [[[FLOOR for z in range(9)] for y in range(max_y)] for x in range(max_x)]
#     for x in range(max_x):
#         inc_last = FLOOR
#         dec_last = FLOOR
#
#         do_diag(grid, size, record, (x, 0),  1)
#         do_diag(grid, size, record, (x, 0), -1)
#
#         for y in range(max_y):
#             inc_y, dec_y = y, max_y - y - 1
#             record[x][inc_y][0] = inc_last
#             record[x][dec_y][1] = dec_last
#
#             inc_last = update_last(inc_last, grid[x][inc_y])
#             dec_last = update_last(dec_last, grid[x][dec_y])
#     for y in range(max_y):
#         inc_last = FLOOR
#         dec_last = FLOOR
#
#         for x in range(max_x):
#             inc_x, dec_x = x, max_x - x - 1
#             record[inc_x][y][2] = inc_last
#             record[dec_x][y][3] = dec_last
#
#             inc_last = update_last(inc_last, grid[inc_x][y])
#             dec_last = update_last(dec_last, grid[dec_x][y])
#
#
#
#     return record

def find_visible(size, grid, x, y, dx, dy):
    cx, cy = x+dx, y+dy
    max_x, max_y = size
    while 0 <= cx < max_x and 0 <= cy < max_y:
        if grid[cx][cy] != FLOOR:
            return  grid[cx][cy]
        cx, cy = cx+dx, cy+dy
    return FLOOR

def part2(grid):
#     record = defaultdict(lambda: defaultdict(str))
#
#
#     record = pre_process_grid(grid, size)
#
#     pp(record)
#     #pp([list(v.values()) for v in dict(record).values()])
    return execute(grid,
                   partial(count_rule,
                           partial(find_visible, grid_size(grid))),
                   5)



# --- Execute the stuff ---
#      (Boiler plate)

# Assumes that input comes in packets of lines, separated by a double newline.
def read_packets(file):
    data =  file.read().strip()  # Get rid of trailing newlines; the don't matter
    packets = [s.split('\n') for s in data.split('\n\n')]

    return packets

# Just split the input on newline and return all the lines raw
def read_lines(f):
    return f.read().splitlines()


print("\n -- Setup --")
if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)
with open(sys.argv[1]) as f:
    # input = read_lines(f)
    input = read_lines(f)

def setup(input):
    return input

print("\n -- Part 1 --")
p1_out = part1(setup(input))

print("\n -- Part 2 --")
p2_out = part2(setup(input))

print("\n -- Results --")
print("Part 1:")
print("  ", p1_out)
print()
print("Part 2:")
print("  ", p2_out)
