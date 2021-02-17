import re
def main():
    with open("advent-of-code-2020/day-16/input.txt") as f:
        input_sections = f.read().split('\n\n')
    rules_predecessor = input_sections[0].split('\n')
    #we'll build rules later, first our ticket...
    our_ticket_predecessor = input_sections[1].split('\n')[1]
    our_ticket = [int(x) for x in our_ticket_predecessor.split(',')]
    #...then the others
    other_tickets_predecessor = input_sections[2].split('\n')[1:]
    other_tickets = [[int(x) for x in t.split(',')] for t in other_tickets_predecessor]

    #can cheese the hell out of rules here
    bounds = [-1, -1, -1, -1]
    for r in rules_predecessor:
        nums = [int(num) for num in re.findall(r'\d+', r)]
        for i in range(4):
            if bounds[i] == -1:
                bounds[i] = nums[i]
            elif i%2 == 0 and nums[i] < bounds[i]:
                bounds[i] = nums[i]
            elif i%2 == 1 and nums[i] > bounds[i]:
                bounds[i] = nums[i]
    
    #rules is just one pair of pairs of bounds that likely overlaps
    #a manual inspection of our input shows there is an overlap,
    #but no need to count on that
    scanning_error_rate = 0
    for tick in other_tickets:
        for n in tick:
            if n < bounds[0] or n > bounds[1] and n < bounds[2] or n > bounds[3]:
                scanning_error_rate += n

    print(scanning_error_rate)

if __name__ == "__main__":
    main()