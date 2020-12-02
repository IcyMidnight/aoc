#!/usr/bin/python3

import sys
import re

if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)

filename = sys.argv[1]

with open(filename) as f:
    lines = f.read().splitlines()

def part1():
    for line in lines:
        print(line)
    return "Part 1"

def part2():

    return "Part 2"



# Actually do the stuff

p1_out = part1()
p2_out = part2()

print("----------------")
print(p1_out)
print(p2_out)
