#!/usr/bin/env python

import sys

def find_basement(line):
    floor = 0
    count = 0
    for c in line:
        count += 1
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            raise RuntimeError("Invalid input: \"%s\" - '%s'" % (line, c))
        if floor < 0:
            return count
    return -1

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        print "%s = position %d" % (line, find_basement(line))
