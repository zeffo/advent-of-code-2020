with open('input.txt') as f:
    data = f.readlines()

    valid, invalid = 0, 0

    for p in data:
        matches = 0
        policy, password = p.split(': ')
        i1, i2 = [int(i) for i in policy[:-1].split('-')]
        letter = policy[-1]
        if password[i1-1] == letter: matches += 1 
        if password[i2-1] == letter: matches += 1
        if matches == 1:
            valid += 1
        else:
            invalid += 1

    print(valid, invalid)
