# Solution to the classic puzzle here: https://fivethirtyeight.com/features/can-you-track-the-delirious-ducks/

import random
from statistics import mean

grid = {1: [2, 4],
        2: [1, 3, 5],
        3: [2, 6],
        4: [1, 5, 7],
        5: [2, 4, 6, 8],
        6: [3, 5, 9],
        7: [4, 8],
        8: [5, 7, 9],
        9: [6, 8]}

def move(locs) -> int:
    "Given a location on a 3x3 grid specified as 1 - 9, return a new location on the grid to move to."
    return [random.choice(grid[loc]) for loc in locs]

def onSameLoc(locs) -> bool:
    "Given two locations, return True if the are the same."
    return all([loc == locs[0] for loc in locs])

def montecarlo(n=2, N=100000):
    "Run a Monte Carlo simulation to determine the average time it takes for two ducks to end up on the same location."
    results = []
    for _ in range(N):
        results.append(findTime(n))
    return mean(results)

def findTime(n=2) -> int:
    "Return the time it takes for two ducks to meet again."
    ducks = [5] * n
    time = 0
    while True:
        ducks = move(ducks)
        time += 1
        if onSameLoc(ducks): return time

def report(n):
    for i in range(2, n + 1):
        print("Mean time for {} ducks: {}".format(i, montecarlo(i)))

report(5)
