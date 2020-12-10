#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp

from collections import defaultdict

# --- Soltuion ---

REQ_REGEX = re.compile("(\d+) (.+) bag")
def parse_rule(line):
    container, rest = line.split(" bags contain ")
    if rest == "no other bags.":
        reqs = []
    else:
        reqs = []
        for req in rest.split(", "):
            m = REQ_REGEX.match(req)
            num, colour = m.groups()
            # print("{}x {}".format(num, colour))
            reqs.append((int(num), colour))
    return (container, reqs)

def build_rules(data):
    rules = {}
    for i, line in enumerate(data):
        container, reqs = parse_rule(line)
        # Assumes there only one rule for each bag colour
        rules[container] = reqs

    return rules

def get_all_containers(rules, colour, work):
    work.add(colour)
    for container, reqs in rules.items():
        if container not in work:
            for n, req in reqs:
                if req == colour:
                    work.add(container)
                    get_all_containers(rules, container, work)

def part1(data):
    rules = build_rules(data)
    # print(rules)

    possibilities = set()
    get_all_containers(rules, "shiny gold", possibilities)

    # print(possibilities)

    return len(possibilities) - 1

def count_bags(rules, colour):
    # print("> Counting {}".format(colour))
    reqs = rules[colour]
    count = 0
    for n, req in reqs:
        # print("{}x {}".format(n, req))
        count += n * (1 +count_bags(rules, req))
    # print("< Count for {} is {}".format(colour, count))
    return count

def part2(data):
    rules = build_rules(data)

    return count_bags(rules, "shiny gold")



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
