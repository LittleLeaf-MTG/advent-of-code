import re

def main():

    #valid_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    count = 0
    with open("advent-of-code-2020/day-4/input.txt") as f:
        for passport_text in f.read().split('\n\n'):
            passport = re.split(r"\s", passport_text)
            passport_fields = dict(field.split(":") for field in passport if field)
            try:
                height = int(passport_fields["hgt"][:-2])
                measurement = passport_fields["hgt"][-2:]
                if all([
                    2002 >= int(passport_fields["byr"]) >= 1920,
                    2020 >= int(passport_fields["iyr"]) >= 2010,
                    2030 >= int(passport_fields["eyr"]) >= 2020,
                    (193 >= height >= 150 and measurement == "cm") or (76 >= height >= 59 and measurement == "in"),
                    re.fullmatch(r"#[\da-f]{6}", passport_fields["hcl"]),
                    passport_fields["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
                    re.fullmatch(r"[\d]{9}", passport_fields["pid"])
                ]):
                    count += 1
            except:
                pass
               
    print(count)

if __name__ == "__main__":
    main()