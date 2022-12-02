#!/usr/bin/env python3

import sys
from collections import defaultdict, Counter, deque

from pprint import pp

import re
import math

DECODE = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

BEATS = {
    'rock':     'paper',
    'paper':    'scissors',
    'scissors': 'rock',
}

SCORE = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

def play_game(game):
    a = DECODE[game[0]]
    x = DECODE[game[1]]
    print('{} {} {}'.format(a, x, BEATS[a]))
    play_score = SCORE[x]
    if a == x:
        outcome = 'tie'
        outcome_score = 3
    elif BEATS[a] == x:
        outcome = 'win'
        outcome_score = 6
    else:
        outcome = 'loss'
        outcome_score = 0

    score = play_score + outcome_score
    print('Game ({},{}) outcome: {} (({}) + ({}) = {})'.format(a, x, outcome, play_score, outcome_score, score))
    return score

def play(strat):
    scores = [play_game(game) for game in strat]
    pp(scores)
    return sum(scores)

def main(args):
    # data = [x.strip().split('\n') for x in sys.stdin.read().split('\n\n')]
    # data = [int(s.strip()) for s in sys.stdin]
    if len(sys.argv) != 2:
        print('Provide the filename')
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().split('\n')

    strat = [tuple(line.split(' ')) for line in lines]

    pp(play(strat))



if __name__ == '__main__':
    main(sys.argv)
