from string import ascii_lowercase


def collapse(string):
    """ Collapses a polymer string according to the challenge details"""
    output = ""
    for char in string:
        prev = "" if not output else output[-1]
        if char.lower() == prev.lower() and char != prev:
            output = output[:-1]
        else:
            output += char
    return output


def main():
    with open("./input.txt", mode="r") as f:
        data = f.readline().strip()

    ###########################################################################
    # PART 1
    ###########################################################################
    p1 = collapse(data)
    print(f"Collapsed Base String Length: {len(p1)}")

    ###########################################################################
    # PART 2
    ###########################################################################
    results = dict()
    for char in ascii_lowercase:
        modified_data = data
        modified_data = modified_data.replace(char, "")
        modified_data = modified_data.replace(char.upper(), "")

        results[char] = len(collapse(modified_data))
    winner = sorted(results, key=lambda x: results[x])[0]
    print(f"Best collapse with character '{winner}' final size: {results[winner]}")


if __name__ == "__main__":
    main()
