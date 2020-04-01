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
    nodes = []
    if node is not None:
       nodes += [node.data]
       nodes += preorder(node.left)
       nodes += preorder(node.right)
    else:
       nodes += ['\n']
    return nodes
    

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
serialized_nodes = preorder(root)

print("serialized_nodes:", serialized_nodes)

#['F', 'B', 'A', '\n', '\n', 'D', 'C', '\n', '\n', 'E', '\n', '\n', 'G', '\n', 'I', 'H', '\n', '\n', '\n']

def construct_tree(nodes, current):
    position = 0
    if nodes[0] != '\n':
       if current is None:
          current = Node(nodes[0])
       
       current.left, nodes = construct_tree(nodes[position+1:], current.left)
       current.right, nodes = construct_tree(nodes[position+1:], current.right)

    else:
       current = None
    return current, nodes

current, nodes = construct_tree(serialized_nodes, None) 

preorder_nodes = preorder(current)
print(preorder_nodes)
