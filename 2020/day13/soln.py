#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp

import math

# --- Soltuion ---

def iterate_time(limit, t):
    end = 0
    while end < limit:
        end += t
    return end

def part1(data):
    time = int(data[0])
    routes = sorted([int(n) for n in data[1].split(",") if n !="x"])
    print(time)
    print(routes)

    next_arrival = [iterate_time(time, r) for r in routes]
    first_dep = min(next_arrival)
    route = routes[next_arrival.index(first_dep)]
    diff = first_dep - time

    return diff * route

def iterate_at(routes, times, pos):
    return

def part2(data):
    routes = [int(n) if n != "x" else n for n in data[1].split(",")]
    print(routes)
    times = list(routes)

    if len(routes) > 10:
        mult = math.ceil(100000000000000 / routes[0])
        times[0] = routes[0] * mult
        print("{} x {} = {}".format(routes[0], mult, times[0]))

    # Seems like things will go way faster if we start iterating the biggest
    # route first, for sort the routes and attach their index.
    sorted_routes = list(reversed(sorted([(int(r), i+1) for i, r in enumerate(routes[1:]) if r != "x"])))
    print(sorted_routes)

    iterations=0
    while True:
        if not iterations % 1000000:
            print("{}: {}".format(iterations, [n for n in times if n != "x"]))
        iterations += 1

        solved = True
        for r, i in sorted_routes:
            desired = times[0] + i
            #print(" {}: {} - {}".format(i, n, desired))
            n = times[i]
            if n > desired:
                #print("n too high")
                target_base = n - i
                mult = math.ceil(target_base / routes[0])
                times[0] = routes[0] * mult
                # print("n:{} d:{}")
                solved = False
                break
            if n < desired:
                #print("n too low")
                mult = math.ceil(desired / routes[i])
                #times[i] = routes[i] * mult
                times[i] = routes[i] * mult
                # while times[i] < desired:
                #     times[i] += routes[i]
                # if one != times[i]:
                #     print("{}: {} vs {}".format(routes[i], one, times[i]))
                #     print("    {} vs {}".format(mult, desired / routes[i]))
                solved = False
                break
        if solved:
            return times[0]


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
