from collections import Counter


def main():
    twos = 0
    threes = 0
    with open("./input.txt", mode="r") as input:
        for line in input:
            c = Counter(line)
            two = three = False
            for char in c:
                if not two and c[char] == 2:
                    two = True
                if not three and c[char] == 3:
                    three = True
            if two:
                twos += 1
            if three:
                threes += 1
    print(twos, threes, twos * threes)


if __name__ == "__main__":
    main()
