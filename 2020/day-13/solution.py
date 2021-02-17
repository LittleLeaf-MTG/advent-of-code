import re
import itertools
def main():

    bus_intervals = []
    with open("advent-of-code-2020/day-13/input.txt") as f:
        fin = f.read().split("\n")
    arrival_time = int(fin[0].strip())
    buses = fin[1].strip()

    bus_intervals = re.findall(r"\d+", buses)

    for steps in itertools.count(0, 1):
        time = arrival_time + steps
        for i in range(len(bus_intervals)):
            if time % int(bus_intervals[i]) == 0:
                print(steps * int(bus_intervals[i]))
                exit()



if __name__ == "__main__":
    main()