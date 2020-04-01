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
root.right.left = Node(6)
root.right.left.right = Node(8)
root.right.right = Node(7)


def width(node):
    if node is None:
       return 0
    else:
       lwidth = width_left(node.left) + 1
       rwidth = width_right(node.right) + 1
    return lwidth, rwidth

def width_left(node):

    if node is None:
       return -1

    else:
       return width_left(node.left) + 1

def width_right(node):
    if node is None:
       return -1

    else:
       return width_right(node.right) + 1


l, r  = width(root)
print("width of tree:", l+r+1)


def vertical_order(node):
    l, r = width(node)
    for i in range(-1*l, r+1):
        current  = 0
        nodes = printVertical(node, i, current)
        print(nodes)


def printVertical(node, level, current):
    nodes = []
    if level == current:
       if node is not None:
          nodes += [node.data]
    if node.left is not None:
       nodes += printVertical(node.left, level, current-1)

    if node.right is not None:
       nodes += printVertical(node.right, level, current+1)
    return nodes

vertical_order(root)
       
    
