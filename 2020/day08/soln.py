#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp



# --- Soltuion ---

def parse_inst(s):
    op, arg = s.split(" ")
    return (op, int(arg))

def exec_detect_loop(instrs):
    prog_size = len(instrs)
    executed = [False] * prog_size

    proc = {
        "nop": lambda arg: (i +   1, acc),
        "acc": lambda arg: (i +   1, acc + arg),
        "jmp": lambda arg: (i + arg, acc),
    }

    i = 0
    acc = 0

    while i < prog_size:
        if executed[i]:
            return prev_i, acc

        executed[i] = True
        prev_i = i

        op, arg = instrs[i]
        i, acc = proc[op](arg)

    return i, acc

def part1(data):
    instrs = [parse_inst(inst) for inst in data]
    # for i, inst in enumerate(data):
    #     print("{}: {}".format(i,inst))

    index, acc = exec_detect_loop(instrs)

    return acc

def part2(data):
    instrs = [parse_inst(inst) for inst in data]
    # for i, inst in enumerate(data):
    #     print("{}: {}".format(i,inst))

    for i in range(len(instrs)):
        op, arg = instrs[i]
        if op == "nop":
            instrs[i] = ("jmp", arg)
        elif op == "jmp":
            instrs[i] = ("nop", arg)
        else:
            continue

        index, acc = exec_detect_loop(instrs)
        if index == len(instrs):
            return acc
        instrs[i] = (op, arg)

    return acc



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
