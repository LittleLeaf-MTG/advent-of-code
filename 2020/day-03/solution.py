def increment_for_slope(course, sx, sy):
    x = y = 0
    count = 0
    while y < len(course):
        if course[y][x] == '#':
            count += 1
        x += sx
        x = x % len(course[y])
        y += sy
    return count

def main():
    x = 0
    with open("advent-of-code-2020/day-3/input.txt") as f:
        slalom = [line.strip() for line in f]
    print(increment_for_slope(slalom, 3, 1))
    
if __name__ == "__main__":
    main()