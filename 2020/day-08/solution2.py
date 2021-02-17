#CURRENTLY INCOMPLETE
#WILL REVISIT AT A LATER DATE
#NOT STARRED ON ADVENT OF CODE


import re

def run_inst(instruction_set) -> {bool, int}:

    pointer = 0
    acc = 0

    while True:
        
        if pointer >= len(instruction_set):
            return {True, acc}
        elif len(instruction_set[pointer]) > 1:
            return {False, acc}
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

def main():

    
    count = 0
    original_instruction_set = {}
    with open("advent-of-code-2020/day-8/input.txt") as f:
        for line in f:
            original_instruction_set[count] = {line.rstrip()}
            count += 1
    

    meta_pointer = 0

    for i in range(len(original_instruction_set)):
        new_instruction_set = original_instruction_set.copy()
        for x in new_instruction_set[meta_pointer]:  
            temp = x.split()        
            op = temp[0]
            arg = int(temp[1])
            if op == "nop":
                new_instruction_set[meta_pointer] = "jmp " + str(arg)            
            elif op == "jmp":
                new_instruction_set[meta_pointer] = "nop " + str(arg)
            
        result = run_inst(new_instruction_set)
        if True in result:
            print(result)
        meta_pointer += 1



    
            
            
        
        
        


if __name__ == "__main__":
    main()