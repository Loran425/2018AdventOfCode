from Utils import timing


def main():
    sum = 0
    iter_counter = 0
    past_sums = []
    modifiers = [int(x) for x in open("./input.txt", mode="r").readlines()]
    while True:
        running_time = timing.time() - timing.start
        print(
            f"[{running_time:9.5f}] Iteration {iter_counter:3}, past_sums length: {len(past_sums):7}"
        )
        for mod in modifiers:
            sum += mod
            if sum in past_sums:
                return sum
            else:
                past_sums.append(sum)
        iter_counter += 1


if __name__ == "__main__":
    print(main())
