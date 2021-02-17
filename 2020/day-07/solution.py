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
    def check_for_shiny_gold(bag_color) -> bool:
        inner_bags = bag_types[bag_color].keys()
        return "shiny gold" in inner_bags or any(check_for_shiny_gold(b) for b in inner_bags)



    print(sum(check_for_shiny_gold(b) for b in bag_types))


if __name__ == "__main__":
    main()