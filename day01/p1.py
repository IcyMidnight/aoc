#!/usr/bin/env python

import sys

def count_floor(line):
    count = 0
    for c in line:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        else:
            raise RuntimeError("Invalid input: \"%s\" - '%s'" % (line, c))
    return count

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.rstrip()
        print "%s = floor %d" % (line, count_floor(line))
