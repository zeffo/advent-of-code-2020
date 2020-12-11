import math
import itertools

with open('input.txt') as i:
    data = [int(n) for n in i.readlines()]

for t in itertools.permutations(data, 3):
    if sum(t) == 2020:
        print(f'Answer: {math.prod(t)}')
        break
    

