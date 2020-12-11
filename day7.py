
class Bag:
    def __init__(self, **data):
        self.quality, self.color = data['name'].split()
        self.contains = data['contains'] # {qual+color: quantity}
        self.name = self.quality+' '+self.color
        self.can_hold = True if 'shiny gold' in self.contains.keys() else False
        
    def __contains__(self, item):
        return item in self.contains.keys()

    def __eq__(self, item):
        return item == self.quality+' '+self.color

    def __repr__(self):
        return self.quality+' '+self.color
    
    def parents(self, bags):
        c = []
        for b in bags.values():
            if str(self) in b:
                c.append(b)
        return c

    def family(self, bags):
        total = []
        for p in self.parents(bags):
            total.append(p)
            total += p.family(bags)
        return total

    def children(self, bags):
        total = 0
        for n, c in self.contains.items():
            total += c
            total += c*bags.get(n).children(bags)
        return total

def add_bag(data):
    name = data.pop(0)
    data = data[0].split(', ')
    contains = {} if data[0] == 'no other bags.' else {' '.join(s.split()[1:-1]): int(s.split()[0]) for s in data}
    return Bag(name=name, contains=contains)

with open('input.txt') as f:
    data = f.read().split('\n')

bags = {}
for bag in data:
    bdata = [s.strip() for s in bag.split('bags contain')]
    if bdata[0] not in bags:
        # print(bdata[0])
        b = add_bag(bdata)
        bags[b.name] = b

b = bags.get('shiny gold')
print(b.children(bags))





    

    
        












