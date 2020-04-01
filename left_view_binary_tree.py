class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
#root.left.left = Node(4)
#root.left.right = Node(5)
root.right.right = Node(4)
root.right.right.right = Node(5)
root.right.right.right.right = Node(6)


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
        nodes = printLevel(node, i, False)
        nodes = [n for n in nodes if n is not None]
        if len(nodes) !=0:
           print(nodes[0])

def printLevel(node, level, printed):
    all_nodes = []
    if level == 0:
       if node is not None:
          all_nodes.append(node.data)
       else:
          all_nodes.append(None)
    else:
       if not printed and node.left is not None:
          all_nodes +=  printLevel(node.left, level-1, printed)
       if not printed and node.right is not None:
          all_nodes += printLevel(node.right, level-1, printed)
    return all_nodes

level_order(root)
