import itertools

with open('input.txt') as f:
    data = [int(n) for n in f.read().split('\n')]

preamble_len = 25

preamble = data[:preamble_len]
total = {}

def find_invalid():
    for index0 in range(preamble_len, len(data)):
        for index1 in range(preamble_len):
            for index2 in range(index1+1, preamble_len):
                total[preamble[index1]+preamble[index2]] = index1+index2
        if not total.get(data[index0]):
            return data[index0], index0
        preamble.pop(0)
        preamble.append(data[index0])
        total.clear()

invalid_num, invalid_index = find_invalid()
print(invalid_index, invalid_num)

def find_set():
    nums = []
    for index1 in range(len(data)):
        nums.append(data[index1])
        for index2 in range(index1+1, len(data)):
            nums.append(data[index2])
            s = sum(nums)
            if s == invalid_num:
                return nums
            elif s > invalid_num:
                nums.clear()
                break


nums = find_set()
print(min(nums)+max(nums))


        