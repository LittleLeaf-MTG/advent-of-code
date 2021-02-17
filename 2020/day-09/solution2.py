import numpy as np


def main():

    target = 556543474
    first = 0
    second = 1
    index = 0
    main_array = np.zeros(1000, dtype=int)
    with open("advent-of-code-2020/day-9/input.txt") as f:
        for line in f:
            main_array[index] = int(line)
            index += 1

    current = main_array[0] + main_array[1]

    while current != target:
        if current < target:
            second += 1
            current += main_array[second]
        elif current > target:
            current -= main_array[first]
            first += 1
        
        

    max_to_print = main_array[first:second + 1].max()
    min_to_print = main_array[first:second + 1].min()

    print(min_to_print + max_to_print)













def problem1():

    main_array = np.zeros(1000, dtype=int)
    index = 0
    buffer = np.zeros(25, dtype=int)
    with open("advent-of-code-2020/day-9/input.txt") as f:
        for line in f:
            main_array[index] = int(line)
            index += 1
    
    #initialize the buffer
    
    for i in range(25):
        buffer[i] = main_array[i]
    
    index = 25      #26th element, first beyond the preamble

    while index <= 1000:
        new_term = main_array[index]
        found_sum = False
        for i in range(25):
            for j in range(25):
                if new_term == buffer[i] + buffer[j] and buffer[i] != buffer[j]:
                    found_sum = True
        if not found_sum:
            print(main_array[index])
            break
        else:
            temp_buffer = np.zeros(25, dtype=int)
            temp_buffer[0:24] = buffer[1:]
            temp_buffer[24] = new_term
            buffer = temp_buffer
            index += 1
        




if __name__ == "__main__":
    main()