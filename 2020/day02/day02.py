#!/usr/bin/python3

import sys
import re

if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)

filename = sys.argv[1]

with open(filename) as f:
    lines = f.read().splitlines()

SLED_REGEX = re.compile("(\d+)-(\d+) (.): (.+)")
def validate_password_sled(string):
    m = SLED_REGEX.match(string)

    minc = int(m.group(1))
    maxc = int(m.group(2))
    char = m.group(3)
    password = m.group(4)

    count = 0
    for c in password:
        if c == char:
            count = count + 1
    passes = count >= minc and count <= maxc
    return passes

TOBOGGAN_REGEX = re.compile("(\d+)-(\d+) (.): (.+)")
def validate_password_toboggan(string):
    m = TOBOGGAN_REGEX.match(string)

    pos1 = int(m.group(1))
    pos2 = int(m.group(2))
    char = m.group(3)
    password = m.group(4)

    # print(" {} {} {}".format(pos1, pos2, char))

    char1 = password[pos1-1]
    char2 = password[pos2-1]

    char1_match = char1 == char
    char2_match = char2 == char

    passes = (char1_match or char2_match) and not (char1_match and char2_match)

    #print("{}: {}-{}, {}-{} -> {}".format(string, char1, char1_match, char2, char2_match, passes))

    return passes

def part1():
    count = 0
    for line in lines:
        if validate_password_sled(line.strip()):
            count = count + 1
    print ("Part 1 passed: {}".format(count))

    return

def part2():
    count = 0
    for line in lines:
        if validate_password_toboggan(line.strip()):
            count = count + 1
    print ("Part 2 passed: {}".format(count))

    return


part1()
part2()
