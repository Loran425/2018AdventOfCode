from collections import Counter
def main():
    strings = [s.strip() for s in open('./input.txt', mode='r').readlines()]
    for string in strings:
        for check in strings:
            if not string and not check:
                break
            diffs = 0
            if string == check:
                continue
            for i in range(len(check)):
                if string[i] != check[i]:
                    diffs += 1
                if diffs > 1:
                    continue
            if diffs == 1:
                print(string)
                print(check)
                return


if __name__ == '__main__':
    main()