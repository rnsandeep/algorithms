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

def preOrder(root):
    nodes = []
    if root is not None:
       nodes += [root.data]
       nodes += preOrder(root.left)
       nodes += preOrder(root.right)
    else:
       nodes += ['\n']

    return nodes

def inOrder(root):
    nodes = []
    if root is not None:
       nodes += inOrder(root.left)
       nodes += [root.data]
       nodes += inOrder(root.right)
    else:
       nodes += ['\n']

    return nodes

# preOrder: ['F', 'B', 'A', '\n', '\n', 'D', 'C', '\n', '\n', 'E', '\n', '\n', 'G', '\n', 'I', 'H', '\n', '\n', '\n']
# inOrder : ['\n', 'A', '\n', 'B', '\n', 'C', '\n', 'D', '\n', 'E', '\n', 'F', '\n', 'G', '\n', 'H', '\n', 'I', '\n']


print(inOrder(root))

def serialize(root):
    return inOrder(root)

def constructTreePreOrder(nodes, root):


    if len(nodes) == 0:
       return None
    else:
       if nodes[0] != '\n':
          root = Node(nodes[0])
          root.left, nodes = constructTreePreOrder(nodes[1:], root.left)
          root.right, nodes = constructTreePreOrder(nodes[1:], root.right)
       else:
          root = None 

    return root, nodes


def constructTreeInOrder(nodes, root):
    if len(nodes) == 0:
       return None
    else:
       if nodes[0] == '\n':
          root.left = None
       elif type(nodes[0]) is Node:
          root.left = nodes[0]
       else:
          root.left = Node(nodes[0])
       root.data = nodes[1]
       if nodes[2] == '\n':
          root.right = None
       elif type(nodes[2]) is Node:
          root.right = nodes[2]
       else:
          root.right = Node(nodes[2])
          
    nodes = [root] + nodes[3:]
    return nodes



def deserialize(nodes):

    while(len(nodes) >1):
        nodes =  constructTreeInOrder(nodes, Node(5))

    return nodes[0]


nodes = inOrder(deserialize(serialize(root)))

print(nodes)
    
       
