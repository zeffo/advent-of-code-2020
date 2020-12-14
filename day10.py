
with open('input.txt') as f:
    data = [int(i) for i in f.read().split('\n')]
    data.sort()

differences = [data[i+1]-data[i] for i in range(len(data)-1)]

ones = differences.count(1)+1
threes = differences.count(3)+1

# Using Dynamic Programming

memo = {}

def recurse(i):
    if i==len(data)-1:
        return 1
    elif i in memo:
        return memo[i]
    else:
        paths = 0
        for x in range(i+1, len(data)):
            if data[x]-data[i] <= 3:
                paths += recurse(x)
        memo[i] = paths
        return paths

t = 0
for y in range(len(data)):
    if data[y] <= 3:
        t += recurse(y)


print(t)



