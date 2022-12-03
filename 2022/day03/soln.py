#!/usr/bin/env python3

import sys

from pprint import pp

from collections import defaultdict, Counter, deque

import re
import math

def extract(s):
    return [int(x) for x in re.findall(r'(-?\d+).?', s)]

def vadd(v1, v2):
    return tuple(x + y for x, y in zip(v1, v2))

def ichr(i):
    return chr(ord('a') + i)

def iord(c):
    return ord(c.lower()) - ord('a')

def optidx(d, opt=max, nth=0):
    if not isinstance(d, dict):
        d = dict(enumerate(d))
    rv = opt(d.values())
    return [i for i, v in d.items() if v == rv][nth], rv

LETTERS = "abcdefghijklmnopqrstuvwxyz"

UP, RIGHT, DOWN, LEFT = VDIRS = (0, -1), (1, 0), (0, 1), (-1, 0),
DIRS = {'N': UP, 'E': RIGHT, 'S': DOWN, 'W': LEFT }
ALL_DIRS = [(x, y) for x in [-1,0,1] for y in [-1,0,1] if not x == y == 0]

def turn(v, d='left'):
    n = -1 if d == 'left' else 1
    return VDIRS[(VDIRS.index(v) + n + len(VDIRS))%len(VDIRS)]


##############################

def priority(t):
    ot = ord(t)
    if ot < ord('a'):
        return ot - ord('A') + 27
    return ot - ord('a') + 1

def groups_of(col, n):
    # Fun thing I stole from stack overflow.
    # We grab an iterator and then turn it into a tuple of n references to it, zip grabs an entry
    # from each reference, depleting the iterator each time. Nice!
    return zip(*(iter(col),) * n)

def part1(sacks):
    split_sacks = [(sack[:int(len(sack)/2)], sack[int(len(sack)/2):]) for sack in sacks]
    #print(split_sacks)

    sets = [(set(sorted(sack[0])), set(sorted(sack[1]))) for sack in split_sacks]
    #print(sets)

    overlaps = [l.intersection(r) for l, r in sets]
    #print(overlaps)

    priorities = [[priority(t) for t in overlap] for overlap in overlaps]
    #print(priorities)

    the_sum = sum([sum(ps) for ps in priorities])

    return the_sum

def part2(sacks):
    groups = [[set(e) for e in g] for g in groups_of(sacks, 3)]
    #print(groups)

    badges = [list(set.intersection(*g))[0] for g in groups]

    return sum([priority(b) for b in badges])

def main(file):
    data = file.read().strip().split('\n')

    #print(data)

    result = part1(data)
    print('Part 1 {}'.format(result))

    result = part2(data)
    print('Part 2 {}'.format(result))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Provide the filename')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        main(file)
