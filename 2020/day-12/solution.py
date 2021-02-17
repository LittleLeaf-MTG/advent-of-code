def main():

    cardinals = {'0': [0, 1], '1': [1, 0], '2': [0, -1], '3': [-1, 0]}
    facing = [1, 0]
    pos = [0, 0]
    instructions = []

    with open("advent-of-code-2020/day-12/input.txt") as f:
        for line in f:
            instructions.append(line.strip())

    for i in instructions:
        action = i[0:1]
        value = int(i[1:])

        if action == 'N':
            pos[1] += value
        elif action == 'E':
            pos[0] += value
        elif action == 'S':
            pos[1] -= value
        elif action == 'W':
            pos[0] -= value
        elif action == 'F':
            pos[0] += facing[0]*value
            pos[1] += facing[1]*value    
        elif action == 'L':
            indices = [0, 1, 2, 3]
            delta = value//90
            for i in indices:
                if facing == cardinals[str(i)]:
                    facing = cardinals[str(indices[i - delta])]
                    break
        elif action == 'R':
            indices = [0, 1, 2, 3]
            delta = value//90
            for i in indices:
                if facing == cardinals[str(i)]:
                    facing = cardinals[str(indices[(i + delta)%4])]
                    break

    print(pos[0], " ", pos[1], "\nManhattan Distance from origin: ") 
    print(abs(pos[0]) + abs(pos[1]))


if __name__ == "__main__":
    main()