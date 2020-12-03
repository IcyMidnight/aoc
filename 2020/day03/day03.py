#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)

input_filename = sys.argv[1]

def setup():
    with open(input_filename) as f:
        lines = f.read().splitlines()

    terrain = []
    for i, line in enumerate(lines):
        terrain.append(list(line))

    return terrain

def part1(input):
    RIGHT = 3
    DOWN = 1
    trees = count_trees(input, RIGHT, DOWN)
    return "Trees: {}".format(trees)

def part2(input):
    DIRECTIONS = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]

    trees_product = 1
    for direction in DIRECTIONS:
        right, down = direction[0], direction[1]
        trees = count_trees(input, right, down)
        trees_product = trees_product * trees

    return "Trees product: {}".format(trees_product)

def count_trees(terrain, right, down):
    width = len(terrain[0])
    length = len(terrain)

    trees = 0
    x, y = down, right
    encountered = []
    while(x < length):
        char = terrain[x][y]
        encountered.append(char)
        # print("{}: {},{} -> {}".format(terrain[x], x, y, char))
        if char == '#':
            trees = trees + 1
        x = x + down
        y = (y + right) % width
    # print("{},{} -> {}".format(right, down, encountered))
    print("{},{} -> {}".format(right, down, trees))
    return trees



# Actually do the stuff

input = setup()
print(" -- Part 1 --")
p1_out = part1(input)
print(" -- Part 2 --")
p2_out = part2(input)

print("\n  -- End --")
print("Part 1:")
print("  ", p1_out)
print("\nPart 2:")
print("  ", p2_out)
