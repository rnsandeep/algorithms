class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
 
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
             next = current.next
             current.next = prev
             prev = current
             current = next
        self.head = prev

    def printList(self):
        temp = self.head
        while(temp):
          print(temp.data)
          temp = temp.next



a = LinkedList()
a.push(10)
a.push(12)
a.push(14)
a.push(15)
a.printList()
a.reverse()
a.printList()


           
          
        
