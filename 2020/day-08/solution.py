import re

def main():

    pointer = 0
    acc = 0
    count = 0
    instruction_set = {}
    with open("advent-of-code-2020/day-8/input.txt") as f:
        for line in f:
            instruction_set[count] = {line.rstrip()}
            count += 1
    

    while True:
        
        if pointer >= len(instruction_set) or len(instruction_set[pointer]) > 1:
            print(acc)
            break
        else:
            for x in instruction_set[pointer]:  #can only ever be the original line (I hope xddd)
                temp = x.split()        
                op = temp[0]
                arg = int(temp[1])
                inst = instruction_set[pointer]
        if op == "nop":
            inst.add(456745674567)
            pointer += 1
            
        elif op == "acc":
            acc += arg
            inst.add(245632452345)
            pointer += 1
            
        elif op == "jmp":
            inst.add(982374509823745890)
            pointer += arg
            
            
        
        
        


if __name__ == "__main__":
    main()