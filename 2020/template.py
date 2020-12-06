#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp



# --- Soltuion ---

def part1(data):
    for i, packet in enumerate(data):
        for j, line in enumerate(packet):
            print(line)
        print()

    return "NOT DONE"

def part2(data):
    return "NOT DONE"



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
