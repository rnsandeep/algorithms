class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

root.right.right.left = Node(8)
root.right.right.right = Node(9)


def width(root, flag):
    if root is not None:

       if flag == 'left':

           if root.left is not None:
              l_width = width(root.left, 'left') + 1
           else:
              l_width = 0
           return l_width
       else:
           if root.right is not None:
               r_width = width(root.right, 'right') + 1
           else:
               r_width = 0
           return r_width

l_width = width(root, 'left')

r_width = width(root, 'right')

def getNodes(root, i, curr):
    nodes = []
    if root is not None:
        if curr == i:
            nodes += [root.data]
        if root.left is not None:
            nodes += getNodes(root.left, i, curr-1)
        if root.right is not None:
            nodes += getNodes(root.right, i, curr+1)
    return nodes


def printNodes(root, l_w, r_w):
    all_nodes = []
    for i in range(-1*l_w, r_w+1):
        nodes = getNodes(root, i, 0)
        print(nodes)
        all_nodes.append(nodes)


printNodes(root, l_width, r_width)

