#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp



# --- Soltuion ---


# Directions: 0: North, 1: East, 2: Sourth, 3: West
# What are the directions of movement for a given direction?
DIR_MOVES = [
        ( 1,  0),  # North
        ( 0,  1),  # East
        (-1,  0),  # South
        ( 0, -1)   # West
    ]

# Figure out the new direction of the ship from the instruction
def turn1(dirn, inst):
    cw = (inst[0] == 'R')
    degs = int(inst[1:])
    quarter_turns = int(degs/90)
    if not cw:
        quarter_turns *= -1
    return (dirn + quarter_turns) % 4

def exec1(pos, dirn, inst):
    pos = list(pos)
    code = inst[0]
    mag = int(inst[1:])
    if code == "N":
        pos[0] += mag
    elif code == "S":
        pos[0] -= mag
    elif code == "E":
        pos[1] += mag
    elif code == "W":
        pos[1] -= mag
    elif code == "F":
        move = DIR_MOVES[dirn]
        pos[0] += move[0] * mag
        pos[1] += move[1] * mag
    else:
        dirn = turn1(dirn, inst)

    return tuple(pos), dirn

def part1(data):
    pos = (0,0)
    dirn = 1

    for i, line in enumerate(data):
        print(line)
        pos, dirn = exec1(pos, dirn, line)
        print("{} -> {}".format(pos, dirn))


    return abs(pos[0]) + abs(pos[1])

# Rotate a position about the origin.
def turn2(pos, inst):
    cw = (inst[0] == 'R')
    degs = int(inst[1:])
    quarter_turns = int(degs/90)
    rotation = 1j**quarter_turns
    vec = complex(*pos)
    if cw:
        vec = vec * rotation
    else:
        vec = vec / rotation
    return (int(vec.real), int(vec.imag))


def exec2(pos, wp, inst):
    wp  = list(wp)
    print("{} - {} :: {}".format(pos, wp, inst))
    code = inst[0]
    mag = int(inst[1:])
    if code == "N":
        wp[0] += mag
    elif code == "S":
        wp[0] -= mag
    elif code == "E":
        wp[1] += mag
    elif code == "W":
        wp[1] -= mag
    elif code == "F":
        pos = (pos[0] + mag * wp[0], pos[1] + mag * wp[1])
    else:
        wp = turn2(wp, inst)

    return tuple(pos), tuple(wp)


def part2(data):
    pos = (0,0)
    wp  = (1,10)

    for i, line in enumerate(data):
        print(line)
        pos, wp = exec2(pos, wp, line)
        print("{} -> {}".format(pos, wp))


    return abs(pos[0]) + abs(pos[1])



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
