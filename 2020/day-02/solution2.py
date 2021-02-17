def main():
    valid_count = 0
    with open("advent-of-code-2020/day-2/input.txt") as f:
        for line in f:
            
            first_instance = 0
            second_instance = 0
            char = ''
            password = ''
            temp = ''
            on_first = False
            on_second = False
            #this string manipulation feels extremely clunky
            temp = line.partition("-")
            first_instance = temp[0]
            line = temp[2]
            temp = line.partition(" ")
            second_instance = temp[0]
            line = temp[2]
            char = line[0:1]
            password = line[3:]

            if password[int(first_instance) - 1:int(first_instance)] == char:
                on_first = True

            if password[int(second_instance) - 1:int(second_instance)] == char:
                on_second = True
            
            if on_first != on_second:
                valid_count += 1

    print(valid_count)


if __name__ == "__main__":
    main()