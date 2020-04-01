def printNodes(root):
    if root!=None :
       #printNodes(root.Left)
       #print(root.data, end=" ")
       printNodes(root.Left)
       printNodes(root.Right)
       print(root.data, end=" ")
    if root == None:
       print("/", end=" ")

class Node:
    def __init__(self, data):
        self.data = data
        self.Left = None
        self.Right = None

a = Node(5)

a.Left = Node(5)
a.Right = Node(6)

a.Left.Right = Node(10)
a.Left.Left = None
a.Right.Left = Node(11)
a.Right.Right = None

printNodes(a)
