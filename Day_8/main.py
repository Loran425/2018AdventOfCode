from dataclasses import dataclass, field


@dataclass
class Node:
    size_children: int
    size_meta: int
    meta_data: list = field(default_factory=list)
    children: list = field(default_factory=list)

    def meta_sum(self):
        s = 0
        s += sum(self.meta_data)
        for child in self.children:
            s += child.meta_sum()
        return s

    def meta_value(self):
        s = 0
        if not self.children:
            s = sum(self.meta_data)
        else:
            for value in self.meta_data:
                if value and value-1 < len(self.children):
                    s += self.children[value-1].meta_value()
        return s


def process(data):
    children = data.pop(0)
    meta = data.pop(0)
    node = Node(children, meta)
    if children:
        for x in range(children):
            child, data = process(data)
            node.children.append(child)
    for x in range(meta):
        node.meta_data.append(data.pop(0))
    return node, data


def main():
    with open("./input.txt", mode='r') as f:
        data = [int(x) for x in f.readline().split()]
    node, data = process(data)

    ###########################################################################
    # PART 1
    ###########################################################################
    print(f'Sum of all meta data: {node.meta_sum()}')


    ###########################################################################
    # PART 2
    ###########################################################################
    print(f'Value of root node: {node.meta_value()}')


if __name__ == "__main__":
    main()
