from collections import Counter
import itertools
def main():

    active_cubes = set()
    with open("advent-of-code-2020/day-17/input.txt") as f:
        for i, l in enumerate(f):
            for j, c in enumerate(l):
                if c == '#':
                    active_cubes.add((j, i, 0))
    
    for _ in range(6):
        counter = Counter()
        for x, y, z in active_cubes:
            for dx, dy, dz in itertools.product((-1, 0, 1), repeat=3):
                if dx == dy == dz == 0:
                    continue
                counter[(x+dx, y+dy, z+dz)] += 1
        new_active_cubes = set()
        for c, i in counter.items():
            if c in active_cubes and 2 <= i <= 3:
                new_active_cubes.add(c)
            elif c not in active_cubes and i == 3:
                new_active_cubes.add(c)
        active_cubes = new_active_cubes
    
    print(len(active_cubes))



if __name__ == "__main__":
    main()