from copy import deepcopy
import itertools

def main():

    seat_matrix = []

    with open("advent-of-code-2020/day-11/input.txt") as f:
        for line in f:
            seat_matrix.append(list(line.strip()))

    still_mutating = True
    while still_mutating:
        todo_matrix = deepcopy(seat_matrix)
        still_mutating = False
        for y in range(len(todo_matrix)):
            for x in range(len(todo_matrix[0])):
                occupied_count = 0
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):

                        for steps in itertools.count(1):
                            if (y + steps*dy) not in range(len(todo_matrix)) or (x + steps*dx) not in range(len(todo_matrix[0])) or dy == dx == 0:
                                break
                            if seat_matrix[y + steps*dy][x + steps*dx] == '#':
                                occupied_count += 1
                                break
                            if seat_matrix[y + steps*dy][x + steps*dx] == 'L':
                                break
                            

                if seat_matrix[y][x] == 'L' and occupied_count == 0:
                    todo_matrix[y][x] = '#'
                    still_mutating = True
                elif seat_matrix[y][x] == '#' and occupied_count >= 5:
                    todo_matrix[y][x] = 'L'
                    still_mutating = True
        
        seat_matrix = todo_matrix
    print(sum(c == '#' for l in seat_matrix for c in l))




if __name__ == "__main__":
    main()