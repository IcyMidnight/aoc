#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)

filename = sys.argv[1]

expense_file = open(filename, 'r')

expenses = []

for line in expense_file.readlines():
    expenses.append(int(line.strip()))

expenses.sort()

# Part 1
def part1():
    for i in range(0, len(expenses) - 1):
        for j in range(i + 1, len(expenses)):
            val1 = expenses[i]
            val2 = expenses[j]
            if (val1 + val2) == 2020:
                print("{} + {} = 2020".format(val1, val2))
                print("{} x {} = {}".format(val1, val2, val1 * val2))
                return
            elif (val1 + val2) > 2020:
                break

# Part 2
def part2():
    for i in range(0, len(expenses) - 2):
        for j in range(i + 1, len(expenses) - 1):
            val1 = expenses[i]
            val2 = expenses[j]
            if val1 + val2 > 2020:
                break
            for k in range(j + 1, len(expenses)):
                val3 = expenses[k]
                if (val1 + val2 + val3) == 2020:
                    print("{} + {} + {} = 2020".format(val1, val2, val3))
                    print("{} x {} x {} = {}".format(val1, val2, val3, val1 * val2 * val3))
                    return
                elif (val1 + val2 + val3) > 2020:
                    break

part1()
part2()
