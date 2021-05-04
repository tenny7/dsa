# code
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = Node(10)
        self.head.next = Node(20)
        self.head.next.next = Node(30)
        self.head.next.next.next = Node(40)
        self.head.next.next.next.next = Node(50)

    def print_list(self):
        current = self.head
        elements = ""
        while current is not None:
            elements += str(current.data) + " "
            current = current.next
        print(elements)


ll = LinkedList()
ll.print_list()