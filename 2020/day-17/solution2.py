from collections import Counter
import itertools
def main():

    active_hypercubes = set()
    with open("advent-of-code-2020/day-17/input.txt") as f:
        for i, l in enumerate(f):
            for j, c in enumerate(l):
                if c == '#':
                    active_hypercubes.add((j, i, 0, 0))
    
    for _ in range(6):
        counter = Counter()
        for x, y, z, w in active_hypercubes:
            for dx, dy, dz, dw in itertools.product((-1, 0, 1), repeat=4):
                if dx == dy == dz == dw == 0:
                    continue
                counter[(x+dx, y+dy, z+dz, w+dw)] += 1
        new_active_hypercubes = set()
        for c, i in counter.items():
            if c in active_hypercubes and 2 <= i <= 3:
                new_active_hypercubes.add(c)
            elif c not in active_hypercubes and i == 3:
                new_active_hypercubes.add(c)
        active_hypercubes = new_active_hypercubes
    
    print(len(active_hypercubes))



if __name__ == "__main__":
    main()