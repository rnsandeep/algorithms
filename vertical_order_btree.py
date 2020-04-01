class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.left.left = Node(4)
root.right.right = Node(6)


def height(node):
    if node is None:
       return 0
    else:
       lheight = height(node.left)
       rheight = height(node.right)

    if lheight > rheight:
       return lheight + 1
    else:
       return rheight + 1


height_tree = height(root)
print("height of tree:", height_tree)


def level_order(node):
    height_tree = height(node)
    for i in range(height_tree):
        print("printing for level :", i)
        printLevel(node, i)


def printLevel(node, level):
    if level == 0:
       if node is not None:
          print(node.data)
    else:
       if node.left is not None:
          printLevel(node.left, level-1)
       if node.right is not None:
          printLevel(node.right, level-1)

level_order(root)
       
    
