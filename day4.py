#!/usr/bin/env python
import sys
import re
from collections import defaultdict

def trigger_pdb_in_caller(exctype, value, tb):
    import traceback, pdb
    traceback.print_exception(exctype, value, tb)
    print()
    pdb.post_mortem(tb)
sys.excepthook = trigger_pdb_in_caller


ADVENT_DAY = "day4"

def parse_passports(lines):
    passports = []
    current_passport = {}
    for line in lines:
        records = line.split(' ')
        if records[0] == "":
            passports.append(current_passport)
            current_passport = {}
            continue
        
        for record in records:
            [k, v] = record.split(':')
            current_passport[k] = v

    return passports


#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)
VALID_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
ELFY_FIELDS = VALID_FIELDS - set(['cid'])
assert len(VALID_FIELDS) == 8  # verify I didn't typo stuff
assert len(ELFY_FIELDS) == 7

hgt_re = re.compile("^([0-9]*)(cm|in)$")
hcl_re = re.compile("^#[0-9a-f]{6}$")
pid_re = re.compile("^0{,9}[0-9]{,9}$")

def validate_height(hgt):
    m = hgt_re.match(hgt)
    if not m:
        return False
        
    num, unit = (int(m[1]), m[2])
    if unit == "cm":
        return 150 <= num <= 193
    if unit == "in":
        return 59 <= num <= 76


is_valid = {
    'byr': lambda yr: 1920 <= int(yr) <= 2002,
    'iyr': lambda yr: 2010 <= int(yr) <= 2020,
    'eyr': lambda yr: 2020 <= int(yr) <= 2030,
    'hgt': validate_height,
    'hcl': lambda v: hcl_re.match(v),
    'ecl': lambda v: v in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    'pid': lambda v: len(v) == 9 and pid_re.match(v),
    'cid': lambda _: True,
}

def is_valid_or_elfy(passport):
    present_fields = set(passport.keys())
    
    for (k, v) in passport.items():
        if not is_valid[k](v):
            return False

    if present_fields == VALID_FIELDS or present_fields == ELFY_FIELDS:
        return True

    return False
    

def advent():
    lines = []
    with open(f'./{ADVENT_DAY}_input') as infile:
        lines = list(infile.read().splitlines())

    all_passports = parse_passports(lines)
    valid_passports = [
        passport
        for passport in all_passports
        if is_valid_or_elfy(passport)
    ]

    # collect max column size info for formatting
    max_val_widths = defaultdict(int)
    for passport in valid_passports:
        for (col, val) in passport.items():
            max_val_widths[col] = max(max_val_widths[col], len(str(val)))

    for passport in valid_passports:
        keys = passport.keys()
        pad = lambda k, v: (max_val_widths[k] - len(str(v))) + 2

        passport = sorted([f"{k}:{v}{' ' * pad(k, v)}" for (k, v) in passport.items()])
        if "cid" not in keys:
            passport = [
                passport[0],
                f"    {' ' * pad('cid', '')}",
                *passport[1:]
            ]
        print(' '.join(passport))

    print("===================")
    print(f"Found {len(valid_passports)} valid passports (see above)")
    print(f"There were {len(all_passports)} total passports")


if __name__ == "__main__":
    advent()