import math


with open('input.txt') as f:
    data = f.read()

plot = data.split('\n')
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

trees = []

def calc(slope):
    x, y = slope
    row, col = 0, 0
    trees = 0
    while row+1 < len(plot):
        col += x
        row += y
        space = plot[row][col%len(plot[row])]
        if space == '#':
            trees += 1
    return trees

for s in slopes:
    tc = calc(s)
    trees.append(tc)



print(math.prod(trees))