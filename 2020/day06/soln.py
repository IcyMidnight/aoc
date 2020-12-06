#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp

# Soltuion

def do_the_sets(input, base_set, op):
    answers = set(base_set)
    groups = []
    for i, line in enumerate(input):
        if len(line) == 0:
            groups.append(answers)
            answers = set(base_set)
        else:
            answers = op(answers, set(line))

    groups.append(answers)

    # pp(groups)

    return groups

def sum_groups(groups):
    return sum(map(len, groups))

def part1(input):
    groups = do_the_sets(input, "", lambda s1, s2: s1 | s2)

    the_sum = sum_groups(groups)

    return "Sum: {}".format(the_sum)

def part2(input):
    groups = do_the_sets(input, "abcdefghijklmnopqrstuvwxyz", lambda s1, s2: s1 & s2)

    the_sum = sum_groups(groups)

    return "Sum: {}".format(the_sum)



# Execute the stuff
def setup(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

print("\n -- Setup --")
if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)

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
