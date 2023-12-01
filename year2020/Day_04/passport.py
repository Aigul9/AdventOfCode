with open('passport.txt', 'r') as f:
    pp = f.read().split('\n\n')
    pp = [line.replace('\n', ' ').split() for line in pp]
    passports = []
    for person in pp:
        passports.append(dict(data.split(':') for data in person))

passports = [p for p in passports if len(p.keys()) == 8 or (len(p.keys()) == 7 and 'cid' not in p.keys())]
print(len(passports))

ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid = []

for v in passports:
    if (
            1920 <= int(v['byr']) <= 2002 and
            2010 <= int(v['iyr']) <= 2020 and
            2020 <= int(v['eyr']) <= 2030 and
            len(v['hcl']) == 7 and
            v['ecl'] in ecl and
            len(v['pid']) == 9 and
            (v['hgt'][-2:] == 'cm' and 150 <= int(v['hgt'][:-2]) <= 193 or
             v['hgt'][-2:] == 'in' and 59 <= int(v['hgt'][:-2]) <= 76)):
        valid.append(v)

print(len(valid))
