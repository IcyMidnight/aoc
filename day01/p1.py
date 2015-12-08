#!/usr/bin/env python

import sys

def find_floor(line):
    floor = 0
    for c in line:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            raise RuntimeError("Invalid input: \"%s\" - '%s'" % (line, c))
    return floor

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        print "%s = floor %d" % (line, find_floor(line))
