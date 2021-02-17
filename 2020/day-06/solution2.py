def main():

    count = 0
    questions = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    with open("advent-of-code-2020/day-6/input.txt") as f:
        for customs_text in f.read().split('\n\n'):
            passengers_in_group = 1 + customs_text.count('\n')
            customs_text = customs_text.replace('\n', '')   #pesky newlines
            for char in customs_text:
                try:
                    questions[char] += 1
                except:
                    pass                        
            for q in questions.keys():
                if questions[q] == passengers_in_group:
                    count += 1
                questions[q] = 0

    print(count)


if __name__ == "__main__":
    main()