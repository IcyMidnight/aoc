#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp

# --- Soltuion ---

def do_the_sets(packets, base_set, op):
    answers = set(base_set)
    groups = []
    for i, packet in enumerate(input):
        group = set(base_set)
        for j, line in enumerate(packet):
            group = op(group, set(line))
        groups.append(group)

    # pp(groups)

    return groups

def sum_groups(groups):
    return sum(map(len, groups))

def part1(input):
    groups = do_the_sets(input, "", lambda s1, s2: s1 | s2)

    the_sum = sum_groups(groups)

    return "Sum: {}".format(the_sum)

POSSIBLE_ANSWERS = "abcdefghijklmnopqrstuvwxyz"
def part2(input):
    groups = do_the_sets(input, POSSIBLE_ANSWERS, lambda s1, s2: s1 & s2)

    the_sum = sum_groups(groups)

    return "Sum: {}".format(the_sum)



# --- Execute the stuff ---
#      (Boiler plate)

# Assumes that input comes in packets of lines, separated by a double newline.
def read_packets(file):
    data =  file.read().strip()  # Get rid of trailing newlines; the don't matter
    packets = [s.split('\n') for s in data.split('\n\n')]

    return packets

def read_lines(f):
    return f.read().splitlines()


print("\n -- Setup --")
if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)
with open(sys.argv[1]) as f:
    # input = read_lines(f)
    input = read_packets(f)

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
