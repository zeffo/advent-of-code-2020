import re

with open('input.txt') as f:
    data = f.read().split('\n\n')


def hgt_val(i):
    unit = i[-2:]
    if unit == 'cm':
        return 150 <= int(i[:-2]) <= 193
    elif unit == 'in':
        return 59 <= int(i[:-2]) <= 76
    else:
        return False



valid = 0
vf= {'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'), 'pid': lambda x: len(x) == 9, 'eyr': lambda x: 2020 <= int(x) <= 2030, 'hcl': lambda x: bool(re.match(r'^#[0-9a-f]{6}$', x)), 'byr': lambda x: 1920 <= int(x) <= 2002, 'iyr': lambda x: 2010 <= int(x)<= 2020, 'hgt': hgt_val}


for l in data:
    clean = l.replace('\n', ' ')
    fields = clean.split()
    passport = dict(l.split(':') for l in fields)
    if passport.get('cid'):
        passport.pop('cid')
    try:
        if set(vf.keys()).issubset({l.split(':')[0] for l in fields}) and all(vf[k](v) for k, v in passport.items()):
            valid += 1
    except Exception as e:
        print(e)


print(valid)    