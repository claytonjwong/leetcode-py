# https://en.wikipedia.org/wiki/Monty_Hall_problem

import random

N = int(1e5)

door = [1, 2, 3]

same, diff = 0, 0

for _ in range(N):
    prize = random.choice(door)
    guess = random.choice(door)
    empty = set(door) - set([prize, guess])
    same += prize == guess                    # 🙈 keep same choice
    diff += prize != guess                    # 🙉 make diff choice

percent = lambda x: int(100 * x / N)
print(f'same: {same}  {percent(same)}%')
print(f'diff: {diff}  {percent(diff)}%')
# same: 33645  33%
# diff: 66355  66%
