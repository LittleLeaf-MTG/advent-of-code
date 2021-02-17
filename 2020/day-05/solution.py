def main():
    with open("advent-of-code-2020/day-5/input.txt") as f:
        ceiling = 0
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
            if seat > ceiling:
                ceiling = seat

    print(ceiling)







if __name__ == "__main__":
    main()