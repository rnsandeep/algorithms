class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def insert_into_tree(root, node):
    if root is None:
       root = node
    else:
        if root.data > node.data:
           root.left = insert_into_tree(root.left, node)
        else:
           root.right = insert_into_tree(root.right, node)
    return root




root = Node(5)
root = insert_into_tree(root, Node(10))
root = insert_into_tree(root, Node(7))
root = insert_into_tree(root, Node(14))


def inorder(root):

    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

inorder(root)







