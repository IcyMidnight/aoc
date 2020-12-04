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

def part1(input):
    for i, line in enumerate(input):
        print(line)

    return "NOT DONE"

def part2(input):
    return "NOT DONE"



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
