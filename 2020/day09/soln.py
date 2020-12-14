#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp



# --- Soltuion ---

# Lifted from Day 1! :D
def has_sum(s, numbers):
    numbers = sorted(numbers)
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            val1 = numbers[i]
            val2 = numbers[j]
            # print("{} + {} = {} ? {}".format(val1, val2, val1+val2, s))
            if (val1 + val2) == s:
                # print("{} + {} = {}".format(val1, val2, s))
                return True
            elif (val1 + val2) > s:
                break

    return False


def find_xmas_weak_num(numbers, preamble_size):
    p = preamble_size

    # print(numbers)

    for i in range(p, len(numbers)):
        num = numbers[i]
        trailing_nums = numbers[i-p:i]
        if not has_sum(num, trailing_nums):
            return numbers[i]

    return -1

def part1(data):
    preamble_size = 25
    # The example has a shorter preamble
    if len(data) == 20:
        preamble_size = 5
    return find_xmas_weak_num(data, preamble_size)

def part2(weak_num, data):
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            slice = data[i:j]
            if weak_num == sum(slice):
                return min(slice) + max(slice)


    return "Oops."




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
    input = list(map(int, read_lines(f)))

print("\n -- Part 1 --")
p1_out = part1(input)

print("\n -- Part 2 --")
p2_out = part2(p1_out, input)

print("\n -- Results --")
print("Part 1:")
print("  ", p1_out)
print()
print("Part 2:")
print("  ", p2_out)
