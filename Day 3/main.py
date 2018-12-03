
def main():
    ###########################################################################
    # INPUT PROCESSING
    ###########################################################################
    claims = {}
    max_w = 1000
    max_h = 1000
    with open('./input.txt', mode='r') as input:
        for line in input:
            claim, data = line.split("@")
            claim_num = claim.lstrip("#").strip()
            pos, size = data.split(":")
            pos = list(map(int, pos.lstrip().split(",")))
            size = list(map(int, size.strip().split("x")))
            claims[claim_num] = (*pos, *size)
            max_w = max(max_w, pos[0] + size[0])
            max_h = max(max_h, pos[1] + size[1])


    ###########################################################################
    # OVERLAP GRID
    ###########################################################################
    c = [[0 for x in range(max_w)] for y in range(max_h)]
    for claim in claims:
        cl = claims[claim]
        for x in range(cl[0], cl[0] + cl[2]):
            for y in range(cl[1], cl[1] + cl[3]):
                c[y-1][x-1] += 1

    ###########################################################################
    # PART 1 - FIND THE TOTAL AMOUNT OF OVERLAP
    ###########################################################################
    double_claimed = 0
    for row in c:
        # print(row)
        for cell in row:
            if cell > 1:
                double_claimed += 1
    print(f"Material in more than one claim: {double_claimed} in^2")

    ###########################################################################
    # PART 2 - FIND THE INTACT CLAIM
    ###########################################################################
    for claim in claims:
        cl = claims[claim]
        intact = True
        for x in range(cl[0], cl[0] + cl[2]):
            for y in range(cl[1], cl[1] + cl[3]):
                if intact and c[y - 1][x - 1] > 1:
                    intact = False
        if intact:
            print(f"Intact Claim # {claim}")


if __name__ == '__main__':
    main()