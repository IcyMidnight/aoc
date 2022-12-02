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
LOSES_TO = {v: k for k, v in BEATS.items()}

PLAY_SCORE = {
    'rock':     1,
    'paper':    2,
    'scissors': 3,
}
OUTCOME_SCORE = {
    'win':  6,
    'tie':  3,
    'loss': 0,
}

def play_game_p1(game):
    a = DECODE[game[0]]
    x = DECODE[game[1]]

    if a == x:
        outcome = 'tie'
    elif BEATS[a] == x:
        outcome = 'win'
    else:
        outcome = 'loss'

    play_score    = PLAY_SCORE[x]
    outcome_score = OUTCOME_SCORE[outcome]

    score = play_score + outcome_score
    #print('Game ({},{}) outcome: {} (({}) + ({}) = {})'.format(a, x, outcome, play_score, outcome_score, score))
    return score

def play_game_p2(game):
    OUTCOMES = {
        'X': 'loss',
        'Y': 'tie',
        'Z': 'win',
    }

    a = DECODE[game[0]]
    outcome = OUTCOMES[game[1]]
    if outcome == 'tie':
        x = a
    elif outcome == 'win':
        x = BEATS[a]
    else:
        x = LOSES_TO[a]

    play_score    = PLAY_SCORE[x]
    outcome_score = OUTCOME_SCORE[outcome]

    score = play_score + outcome_score
    #print('Game ({},{}) outcome: {} (({}) + ({}) = {})'.format(a, x, outcome, play_score, outcome_score, score))
    return score

def play(strat, player):
    scores = [player(game) for game in strat]
    #pp(scores)
    return sum(scores)

def main(filename):
    with open(filename, 'r') as f:
        data = f.read()

    lines = data.strip().split('\n')

    strat = [tuple(line.split(' ')) for line in lines]

    p1 = play(strat, play_game_p1)
    print('Part 1: {}'.format(p1))

    p2 = play(strat, play_game_p2)
    print('Part 2: {}'.format(p2))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Provide the filename')
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
