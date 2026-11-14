class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(f"Preorder: {preorder(root)}")
    print(f"Inorder: {inorder(root)}")
    print(f"Postorder: {postorder(root)}")


if __name__ == "__main__":
    main()
