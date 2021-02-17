import itertools
def main():
    mem = {}
    with open("advent-of-code-2020/day-14/input.txt") as f:
        instructions = f.read().splitlines()

    for i in instructions:
        i_key, i_value = i.split(" = ")
        if i_key == "mask":
            x_indices = []
            one_indices = [] 
            for i, t in enumerate(reversed(i_value)):
                if t == 'X':
                    x_indices.append(int(i))
                elif t == '1':
                    one_indices.append(int(i))
        else:
            address = int(i_key[4:-1])
            for index in one_indices:
                address |= 1 << index
            for tup in itertools.product((0, 1), repeat=len(x_indices)):
                for t, x in zip(tup, x_indices):
                    if t == 0:
                        address &= ~(1 << x)
                    else:
                        address |= 1 << x
                mem[address] = int(i_value)
    print(sum(mem.values()))




if __name__ == "__main__":
    main()