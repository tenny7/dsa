class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        new_element = Node(data)
        if self.head is None:
            self.head = new_element
        elif self.head is not None:
            current = self.head
            new_element.next = current
            self.head = new_element

    def print_list(self):
        current = self.head
        elements = ""
        while current is not None:
            elements += str(current.data) + "->"
            current = current.next
        print(elements)


ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_beginning(13)
ll.insert_at_beginning(40)

ll.print_list()
