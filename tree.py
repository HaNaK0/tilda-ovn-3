class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left: TreeNode = None
        self.right: TreeNode = None

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def put(self, aNode):
        if self < aNode:
            if self.right is None:
                self.right = aNode
            else:
                self.right.put(aNode)
        else:
            if self.left is None:
                self.left = aNode
            else:
                self.left.put(aNode)


class Tree:
    def __init__(self) -> None:
        self.root: TreeNode = None

    def put(self, aValue) -> None:
        newNode = TreeNode(aValue)

        if self.root is None:
            self.root = newNode
            return

        self.root.put(newNode)


def sum(aNode: TreeNode):
    if aNode is None:
        return 0
    else:
        return aNode.value + sum(aNode.left) + sum(aNode.right)


if __name__ == "__main__":
    numbers = [4, 2, 1, 6, 3, 7, 5]

    tree = Tree()

    for number in numbers:
        tree.put(number)

    print(sum(tree.root))
