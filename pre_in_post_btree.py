class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node('F')
root.left = Node('B')
root.right = Node('G')
root.left.right = Node('D')
root.left.right.left = Node('C')
root.left.right.right = Node('E')
root.left.left = Node('A')
root.right.right = Node('I')
root.right.right.left = Node('H')


def preorder(node):
    if node is not None:
       print(node.data)
       preorder(node.left)
       preorder(node.right)

def inorder(node):
    if node is not None:
       preorder(node.left)
       print(node.data)
       preorder(node.right)

def postorder(node):
    if node is not None:
       preorder(node.left)
       preorder(node.right)
       print(node.data)

print("pre order :")
preorder(root)
print("inorder:")
inorder(root)
print("postorder:")
postorder(root)
