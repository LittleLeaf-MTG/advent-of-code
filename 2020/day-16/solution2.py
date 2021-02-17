import re
from math import prod
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

    
    #cheese-free this time
    rules = {(rsplit := r.split(":"))[0]: [int(num) for num in re.findall(r'\d+', rsplit[1])] for r in rules_predecessor}
    rules_values = list(rules.values())
    bounds = [(min if i % 2 == 0 else max)(r[i] for r in rules_values) for i in range(4)]
    clean_tickets = []

    for tick in other_tickets:
        for n in tick:
            if n < bounds[0] or n > bounds[1] and n < bounds[2] or n > bounds[3]:
                break
        else:
            clean_tickets.append(tick)

    ticket_columns = [list(t) for t in zip(*clean_tickets)]

    rule_indices = {}

    rulesets = {i: validate_column(c, rules) for i, c in enumerate(ticket_columns)}
    while len(rule_indices) != len(rules):
        for i, s in rulesets.items():
            if len(s) == 1:
                valid_rule = s.pop()
                rule_indices[valid_rule] = i
                for se in rulesets.values():
                    se.discard(valid_rule)
                break

    print(prod(our_ticket[x] for i, x in rule_indices.items() if i.startswith("departure")))



def validate_column(col: list, rules: dict) -> set:
    return {r for r, (a, b, c, d) in rules.items() if all(a <= x <= b or c <= x <= d for x in col)}



if __name__ == "__main__":
    main()