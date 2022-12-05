#!/usr/bin/env python3

import sys

from pprint import pp

def set_completely_contains(s1, s2):
    intersection = s1 & s2
    return intersection == s1 or intersection == s2

def part1(ranges):
    completely_contained = [1 if set_completely_contains(s1, s2) else 0 for s1, s2 in ranges]
    #pp(completely_contained)
    return sum(completely_contained)

def part2(ranges):
    overlaps = [1 if s1 & s2 else 0 for s1, s2 in ranges]
    #pp(overlaps)
    return sum(overlaps)

def main(file):
    data = file.read().strip().split('\n')

    #print(data)

    ranges = [(set(range(int(r0[0]), int(r0[1])+1)), set(range(int(r1[0]), int(r1[1])+1)))
              for r0, r1 in [(r.split('-')
                              for r in
                              line.split(','))
                             for line in data]]

    result = part1(ranges)
    print('Part 1 {}'.format(result))

    result = part2(ranges)
    print('Part 2 {}'.format(result))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Provide the filename')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        main(file)
