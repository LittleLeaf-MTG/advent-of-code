def main():
    or_mask = and_mask = None
    mem = {}
    with open("advent-of-code-2020/day-14/input.txt") as f:
        instructions = f.read().splitlines()

    for i in instructions:
        i_type, i_value = i.split(" = ")
        if i_type == "mask":
            or_mask = int(i_value.replace('X', '0'), 2)
            and_mask = int(i_value.replace('X', '1'), 2)
        else:
            mem[int(i_type[4:-1])] = (int(i_value) | or_mask) & and_mask
    
    print(sum(mem.values()))


if __name__ == "__main__":
    main()