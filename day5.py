
with open('input.txt') as f:
    data = f.read().split('\n')

ids =[]

for bpass in data:
    rows = bpass[:-3]
    column = bpass[-3:]
    mapping = {'F': '0' , 'B': '1', 'R': '1', 'L': '0'}
    row = int(''.join(mapping[c] for c in rows), 2)
    col = int(''.join(mapping[c] for c in column), 2)
    seat = (row*8)+col
    ids.append(seat)

ids.sort()
print(ids)
for n, i in enumerate(ids):
    if n+1 < len(ids):
        if i+1 != ids[n+1]:
            print((ids[n+1]+i)/2)
            pass




