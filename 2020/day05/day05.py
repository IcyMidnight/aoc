#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp


if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)

def setup(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def partition(string, less, more):
    e = len(string)
    n = 0

    bin_string = ""


    for c in string:
        n *= 2
        if c == more:
            bin_string += "1"
            n += 1
        else:
            bin_string += "0"
    # print("{} -> {}".format(string, bin_string))
    return n

def calc_seat(boarding_pass):
    row_part, col_part = boarding_pass[:7], boarding_pass[7:]

    row = partition(row_part, "F", "B")
    col = partition(col_part, "L", "R")
    seat = row * 8 + col

    # print("{} {} -> {},{}: {}".format(row_part, col_part, row, col, seat))

    return seat


def find_seats(passes):
    return map(calc_seat, passes)


def part1(input):
    return "Max seat: {}".format(max(find_seats(input)))

def part2(input):
    seats = list(find_seats(input))
    seats.sort()

    for s1, s2 in zip(seats, seats[1:]):
        if s2 != s1 + 1:
            return "Seat: {}".format(s1 + 1)

    return "Plane's full!"


# Actually do the stuff

print("\n -- Setup --")
input = setup(sys.argv[1])

print("\n -- Part 1 --")
p1_out = part1(input)

print("\n -- Part 2 --")
p2_out = part2(input)

print("\n -- Results --")
print("Part 1:")
print("  ", p1_out)
print()
print("Part 2:")
print("  ", p2_out)
