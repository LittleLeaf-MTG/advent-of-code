def main():
    with open("advent-of-code-2020/day-15/input.txt") as f:
        numbers = f.read().split(',')
    index = 0
    memory = []
    while index < len(numbers):
        memory.append((index, int(numbers[index])))
        index += 1
    while index <= 2020:
        num = int(memory[index - 1][1])
        for i, n in reversed(memory):
            if num == n and i != index - 1:
                memory.append((index, (index - i - 1)))
                break
        else:
            memory.append((index, 0))
        index += 1
    print(memory[2019]) #spent far too long wondering why
                        #this didn't work with print(memory[2020])
                        #before realizing I was off by one...


if __name__ == "__main__":
    main()