with open('input.txt') as f:
    data = f.read().split('\n\n')

count = 0
for group in data:
    answers = [set(g) for g in group.split('\n')]
    common = answers[0].intersection(*answers)
    count += len(common)
print(count)