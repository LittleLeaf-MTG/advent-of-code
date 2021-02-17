#reusing very little from solution 1 on the grounds that it was terribly done

def main():

    pos = [0,0]
    waypoint = [10, 1]
    instructions = []

    with open("advent-of-code-2020/day-12/input.txt") as f:
        for line in f:
            instructions.append(line.strip())
    
    for i in instructions:
        action = i[0:1]
        value = int(i[1:])

        if action == 'F':
            pos[0] += waypoint[0]*value
            pos[1] += waypoint[1]*value
        elif action == 'N':
            waypoint[1] += value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'W':
            waypoint[0] -= value
        elif action == 'L':
            x = waypoint[0]
            y = waypoint[1]
            if value == 90:
                waypoint = [-1*y, x]
            elif value == 180:
                waypoint = [-1*x, -1*y]
            elif value == 270:
                waypoint = [y, -1*x]
        elif action == 'R':
            x = waypoint[0]
            y = waypoint[1]
            if value == 90:
                waypoint = [y, -1*x]
            elif value == 180:
                waypoint = [-1*x, -1*y]
            elif value == 270:
                waypoint = [-1*y, x]
        
    print(abs(pos[0]) + abs(pos[1]))



if __name__ == "__main__":
    main()