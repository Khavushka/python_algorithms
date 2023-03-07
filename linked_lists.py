# Linked lists (traverse, search, add, delete, header, nodes, tail)
'''
A linked list is a linear collection of data elements whose order is 
not given by their physical placement in memory. Instead, 
each element points to the next. It's a data structure consisting of 
a collection of nodes which together represent a sequence.

In its most basic form, each node contains: data, and a reference
(in other words, a link) to the next node in the sequence. 

This structure allows for efficicent insertion or removal of elements 
from any position in the sequence during iteration. 

More complex variants add additional links, allowing more efficient
insertion or removal of nodes at arbitrary positions.

A drawback of linked lists is that access time is linear (and difficult to pipeline)
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next
    
    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Jenny")

# Create objects
family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

family.insert_new_header("Dave")

# family.traversal()

family.delete_node('Amy')
family.delete_tail()
family.traversal()