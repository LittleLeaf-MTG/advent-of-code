import re
from functools import lru_cache
def main():
    #each bag will itself be a collection of other
    #bag tokens I guess
    bag_types = {}
    with open("advent-of-code-2020/day-7/input.txt") as f:
        for line in f:
            line_partition = line.split(" bags contain ")
            new_bag_type = line_partition[0]
            sub_bag_types = re.findall(r"(\d+) (.+?) bag", line_partition[1])
            sub_bag_dict = {}
            for bag in sub_bag_types:
                amount = int(bag[0])
                color = bag[1]
                sub_bag_dict[color] = amount
            bag_types[new_bag_type] = sub_bag_dict

    @lru_cache
    def check_within_shiny_gold(bag_color) -> int:
        inner_bags = bag_types[bag_color].items()
        return sum(check_within_shiny_gold(c)*a for c, a in inner_bags) + 1


    print(check_within_shiny_gold("shiny gold") - 1)


if __name__ == "__main__":
    main()