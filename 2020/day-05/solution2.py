def main():
    with open("advent-of-code-2020/day-5/input.txt") as f:
        occupied = []
        for line in f:
            row_bottom = 0
            row_top = 127
            column_bottom = 0
            column_top = 7
            diff = 0
            for char in line:
                if char == 'F':
                    diff = row_top - row_bottom
                    row_top -= (diff // 2 + 1)
                elif char == 'B':
                    diff = row_top - row_bottom
                    row_bottom += (diff // 2 + 1)
                elif char == 'L':
                    diff = column_top - column_bottom
                    column_top -= (diff // 2 + 1)
                elif char == 'R':
                    diff = column_top - column_bottom
                    column_bottom += (diff // 2 + 1)
                elif char.isspace():
                    pass
                else:
                    exit()
            seat = (row_top * 8) + column_top
            occupied.append(seat)
    occupied.sort()
    for i in range(len(occupied) - 1):
        if (occupied[i] - occupied[i + 1]) < -1:
            print(occupied[i] + 1)
            break


if __name__ == "__main__":
    main()