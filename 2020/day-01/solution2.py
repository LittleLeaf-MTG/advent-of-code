def main():
    a = []
    with open("day-1/input.txt") as f:
        for line in f:

            a.append(int(line))

    for first in a:
        for second in a:
            for third in a:
                if (first + second + third) == 2020:
                    print(first * second * third)


if __name__ == "__main__":
    main()