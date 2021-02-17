import re
import itertools
def main():
    bus_intervals = []
    with open("advent-of-code-2020/day-13/input.txt") as f:
        fin = f.read().split("\n")
    
    buses = fin[1].strip()
    bus_list_with_skips = buses.split(",")
    for x in range(len(bus_list_with_skips)):
        if re.match(r"\d+", bus_list_with_skips[x]):
            bus_intervals.append([bus_list_with_skips[x], x])

    timestamp = int(bus_intervals[0][0])
    interval = int(bus_intervals[0][0])
    bus_delta = int(bus_intervals[1][1])
    i = 1

    while bus_delta < len(bus_list_with_skips):
        if (timestamp + bus_delta) % int(bus_intervals[i][0]) == 0:
            interval *= int(bus_intervals[i][0])
            i += 1
            if (i < len(bus_intervals)):
                bus_delta = int(bus_intervals[i][1])
            else:
                break
        else:
            timestamp += interval

    print(timestamp)

if __name__ == "__main__":
    main()