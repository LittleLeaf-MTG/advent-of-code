import re

def main():

    valid_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    passport = []
    passport_text = ''
    count = 0
    with open("advent-of-code-2020/day-4/input.txt") as f:
        for passport_text in f.read().split('\n\n'):
            passport = re.split(r"\s", passport_text)
            passport_fields = dict(field.split(":") for field in passport if field)
            if passport_fields.keys() >= valid_fields:
                count += 1

    print(count)


if __name__ == "__main__":
    main()