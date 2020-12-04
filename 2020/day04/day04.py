#!/usr/bin/python3

import sys
import re
import pprint
pp = pprint.pprint # in pyhton >= 3.8, from pprint import pp

if len(sys.argv) != 2:
    print('Provide the filename')
    sys.exit(1)

def setup(filename):
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def decode_passports(lines):
    passports = []
    passport = {}

    for line in lines:
        if len(line) == 0:
            passports.append(passport)
            passport = {}
        else:
            entries = line.split(" ")
            for entry in entries:
                key, val = entry.split(":")
                passport[key] = val

    passports.append(passport)

    return passports

# cid optional
REQUIRED_KEYS = "byr,iyr,eyr,hgt,hcl,ecl,pid".split(",")

def valid_passport(passport):
    keys = passport.keys()
    valid = all(key in keys for key in REQUIRED_KEYS)

    print("{}: {}".format(valid, passport))

    return valid

PID_REGEX = re.compile("^\d{9}$")
HAIR_REGEX = re.compile("^#[0-9a-f]{6}$")
EYE_COLOURS = "amb blu brn gry grn hzl oth".split(" ")

def validate_strict(ppp):
    try:
        byr = int(ppp["byr"])
        if byr < 1920 or byr > 2002:
            return False, "Birth: {}".format(byr)

        iyr = int(ppp['iyr'])
        if iyr < 2010 or iyr > 2020:
            return False, "Issue: {}".format(iyr)

        eyr = int(ppp['eyr'])
        if eyr < 2020 or eyr > 2030:
            return False, "Expiry {}".format(eyr)

        height, units = int(ppp['hgt'][:-2]), ppp['hgt'][-2:]
        if units == "cm":
            if height < 150 or height > 193:
                return False, "Height cm: {}".format(height)
        elif units == "in":
            if height < 59 or height > 76:
                return False, "Height cm: {}".format(height)
        else:
            return False, "Height bad units"

        if not HAIR_REGEX.match(ppp['hcl']):
            return False, "Hair: {}".format(ppp['hcl'])

        if ppp['ecl'] not in EYE_COLOURS:
            return False, "Eye: {}".format(ppp['ecl'])

        if not PID_REGEX.match(ppp['pid']):
            return False, "PID: {}".format(ppp['pid'])

    except ValueError as e:
        return False, e
    except KeyError as e:
        return False, "Missing key: {}".format(e)


    return True, None

def valid_passport_strict(passport):
    valid, log = validate_strict(passport)

    post = "" if valid else " - {}".format(log)
    print("{}{} - {}".format(valid, post, passport))

    return valid


def part1(input):
    passports = decode_passports(input)

    # pp(passports)

    num_valid = sum(1 for p in passports if valid_passport(p))

    return "Valid: {}".format(num_valid)

def part2(input):
    passports = decode_passports(input)

    # pp(passports)

    num_valid = sum(1 for p in passports if valid_passport_strict(p))

    return "Valid: {}".format(num_valid)


# Actually do the stuff

print("\n -- Setup --")
input = setup(sys.argv[1])

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
