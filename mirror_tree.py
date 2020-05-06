class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



root = Node(5)
root.left = Node(10)
root.left.left = Node(11)
root.left.right = Node(12)

root.right = Node(13)
root.right.left = Node(14)
root.right.right = Node(15)


def inorder(root):
    if root is not None:
       inorder(root.left)
       print(root.data)
       inorder(root.right)


def mirror(root):
    if root is not None:
        if root.left is not None:
            right = mirror(root.left)
        else:
            right = None
        if root.right is not None:
            left = mirror(root.right)
        else:
            left = None

        root.left = left
        root.right = right
    return root



inorder(root)
inorder(mirror(root))
