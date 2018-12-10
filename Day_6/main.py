from PIL import Image


class Map:
    BASE = "#"
    EQD = "0"

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[[Map.BASE] for x in range(width)] for y in range(height)]
        self.dist_grid = [[0 for x in range(width)] for y in range(height)]
        self.points = list()
        self.summary = dict()

    def mark(self, point):
        self.points.append(point)
        self.grid[point.y - 1][point.x - 1] = point.num

    def process(self):
        for y in range(self.height):
            for x in range(self.width):
                base = Point(x, y, Map.BASE)
                dist = list()
                for point in self.points:
                    distance = base.dist(point)
                    dist.append((distance, point.num))
                    self.dist_grid[y][x] = self.dist_grid[y][x] + distance

                min_dist = sorted(dist, key=lambda p: p[0])

                if [d[0] for d in min_dist].count(min_dist[0][0]) == 1:
                    self.grid[y][x] = min_dist[0][1]
                else:
                    self.grid[y][x] = Map.EQD

        for point in self.points:
            self.summary[point.num] = self.area(point.num)

        # Symbols on the boarder are going to be infinite
        for symbol in set(self.grid[0]):
            self.summary[symbol] = -1

        for symbol in set(self.grid[-1]):
            self.summary[symbol] = -1

        # Swap rows and columns
        temp_grid = list(zip(*self.grid))

        for symbol in set(temp_grid[0]):
            self.summary[symbol] = -1

        for symbol in set(temp_grid[-1]):
            self.summary[symbol] = -1

    def area(self, symbol):
        count = 0
        for row in self.grid:
            count += row.count(symbol)
        return count


class Point:
    def __init__(self, x, y, num: str):
        self.x = x
        self.y = y
        self.num = num

    def dist(self, point):
        delta_x = abs(point.x - self.x)
        delta_y = abs(point.y - self.y)
        return delta_y + delta_x

    def __str__(self):
        return self.num

    def __repr__(self):
        return f"Point @ {self.x} {self.y}, marked by {self.num}"


def main():
    ###########################################################################
    # Input Processing
    ###########################################################################

    points = []
    num = 1
    with open("./input.txt", mode="r") as f:
        for line in f:
            x, y = [int(i.strip(",")) for i in line.strip().split()]
            points.append(Point(x, y, str(num)))
            num += 1

    map_size_x = sorted(points, key=lambda p: p.x, reverse=True)[0].x
    map_size_y = sorted(points, key=lambda p: p.y, reverse=True)[0].y

    grid = Map(map_size_x, map_size_y)

    for point in points:
        grid.mark(point)

    grid.process()  # All the Magic happens here

    # Ok Most of it
    areas = grid.summary
    max_area, max_symbol = 0, 0
    for area in areas:
        if areas[area] > max_area:
            max_area = areas[area]
            max_symbol = area

    print(f"Max area of {max_area} found with point #{max_symbol}")

    ###########################################################################
    # DEBUG IMAGE
    ###########################################################################
    img = Image.new("L", (356, 356), color="white")
    data = [int(item) for sublist in grid.grid for item in sublist]
    img.putdata(data, 5)
    for point in points:
        img.putpixel((point.x - 1, point.y - 1), 255)
    img = img.resize((356 * 3, 356 * 3))
    img.show()

    ###########################################################################
    # DEBUG IMAGE 2
    ###########################################################################
    img2 = Image.new("L", (356, 356), color="white")
    data2 = [
        100 if item < 10000 else 0 for sublist in grid.dist_grid for item in sublist
    ]
    img2.putdata(data2)
    for point in points:
        img2.putpixel((point.x - 1, point.y - 1), 255)
    img2 = img2.resize((356 * 3, 356 * 3))
    img2.show()

    print(f"Strategy 2 Safe~ish area size: {data2.count(100)}")

    ###########################################################################
    # Output the images because they look cool
    ###########################################################################

    img.save("Strategy_1_Results.png")
    img2.save("Strategy_2_Results.png")


if __name__ == "__main__":
    main()
