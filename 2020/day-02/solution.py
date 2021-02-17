def main():
    valid_count = 0
    with open("advent-of-code-2020/day-2/input.txt") as f:
        for line in f:
            #aside from char_count is any of this necessary?
            lower_bound = 0
            upper_bound = 0
            char = ''
            password = ''
            temp = ''
            char_count = 0
            #this string manipulation feels extremely clunky
            temp = line.partition("-")
            lower_bound = temp[0]
            line = temp[2]
            temp = line.partition(" ")
            upper_bound = temp[0]
            line = temp[2]
            char = line[0:1]
            password = line[3:]

            for letter in password:
                if letter == char:
                    char_count += 1
            
            if char_count >= int(lower_bound) and char_count <= int(upper_bound):
                valid_count += 1

    print(valid_count)


if __name__ == "__main__":
    main()