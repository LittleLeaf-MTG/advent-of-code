def main():
    a = []
    with open("day-1/input.txt") as f:
        for line in f:

            a.append(int(line))

    for first in a:
        for second in a:
            if (first + second) == 2020:
                print(first * second)


if __name__ == "__main__":
    main()