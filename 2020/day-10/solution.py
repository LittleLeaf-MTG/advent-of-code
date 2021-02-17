def main():

    one_diff_count = 0
    two_diff_count = 0
    three_diff_count = 0
    previous_adapter_jolts = 0
    index = 0
    adapters = []
    
    with open("advent-of-code-2020/day-10/input.txt") as f:
        for line in f:
            adapters.append(int(line.rstrip()))
    
    adapters.sort()


    while index < len(adapters):
        
        current_adapter_jolts = adapters[index]
        if current_adapter_jolts - previous_adapter_jolts == 1:
            one_diff_count += 1
        elif current_adapter_jolts - previous_adapter_jolts == 2:
            two_diff_count += 1
        elif current_adapter_jolts - previous_adapter_jolts == 3:
            three_diff_count += 1
        else:
            print("yikes")
            break
        previous_adapter_jolts = current_adapter_jolts
        index += 1
    
    three_diff_count += 1
    print(one_diff_count * three_diff_count)




if __name__ == "__main__":
    main()