#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp

#from functools import reduce
from collections import defaultdict

# --- Soltuion ---


def device_joltage(sorted_joltages):
    return sorted_joltages[-1] + 3

def find_chain(joltages, chain = [0]):
    # print("{} {}".format(joltages, chain))
    if len(joltages) == 0:
        return chain

    last = 0
    if len(chain) > 0:
        last = chain[-1]

    for i, j in enumerate(joltages):
        if j < last or j >  last + 3:
            continue
        res = find_chain(joltages[:i] + joltages[i+1:], chain + [j])
        if res:
            return res

def dist_diffs(chain):
    dist = defaultdict(int)
    for x, y in  zip(chain, chain[1:]):
        diff = y - x
        # print("{},{} -> {}".format(x,y,diff))
        dist[diff] += 1
    return dict(dist)

def part1(data):
    device = device_joltage(data)
    print("Device: {}".format(device))

    chain = find_chain(data + [device])

    diffs = dist_diffs(chain)

    print(diffs)

    return diffs[1] * diffs[3]

# How many variations are there from the device with a particular joltage to the end.
chain_vars = {}
def count_chains(joltages, chain = [0], last = 0):
    # We used every device. Woo hoo!
    if len(joltages) == 0:
        return 1
    # The last device in joltages can be hopped to from the last device in chain. Good enough!
    if len(chain) > 0 and chain[-1] <= joltages[-1] and chain[-1] + 3 >= joltages[-1]:
        return 1

    chains = 0

    for i, j in enumerate(joltages):
        # We should probably just filter these out so we don't waste time.
        if j < last:
            continue
        # None of the rest of these are going to work
        elif j >  last + 3:
            break

        # We already know how it goes from here
        if j in chain_vars:
            count = chain_vars[j]
        # Figure out how many ways to get from here to the end
        else:
            count = count_chains(joltages[:i] + joltages[i+1:], chain + [j], j)
            chain_vars[j] = count
        chains += count

    return chains

def part2(data):
    device = device_joltage(data)
    print("Device: {}".format(device))

    chains = count_chains(data + [device])

    return chains



# --- Execute the stuff ---
#      (Boiler plate)

# Just split the input on newline and return all the lines raw
def read_lines(f):
    return f.read().splitlines()


print("\n -- Setup --")
if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)
with open(sys.argv[1]) as f:
    input = sorted(list(map(int, read_lines(f))))

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
