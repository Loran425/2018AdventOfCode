def main():
    sum = 0
    with open('./input.txt', mode='r') as input:
        for line in input:
            sum += int(line.strip())
    print(sum)


if __name__ == '__main__':
    main()