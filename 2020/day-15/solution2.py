def main():
    with open("advent-of-code-2020/day-15/input.txt") as f:
        nums = [int(x) for x in f.read().split(',')]
    
    
    table = {x: i for i, x in enumerate(nums[:-1], start=1)}
    current = nums[-1]
    for index in range(len(table) + 1, 30000000):
        if current in table:
            weliketemps = table[current]
            diff = index - weliketemps
        else:
            diff = 0
        table[current] = index
        current = diff
    print(current)
            


if __name__ == "__main__":
    main()