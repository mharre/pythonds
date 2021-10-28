
class Node:

    def __init__(self, cargo=None, nextNode=None):
        self.cargo = cargo
        self.next = nextNode

    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")


class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()

    def add_first(self, cargo):
        node = Node(cargo)
        node.next = self.head
        # print(self.head)
        self.head = node
        self.length += 1

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3


def print_list(node):
    while node is not None:
        print(node, end=' ')
        node = node.next

def remove_second(linkedlist):
    if linkedlist is None: return
    first = linkedlist
    second = linkedlist.next
    #ref to 3rd node, setting first next to the node that is next from second
    first.next = second.next
    second.next = None
    return second

# print_list(node1)
# removed = remove_second(node1)
# print_backward_nicely(node1)