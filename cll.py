# code
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data=None):
        new_element = Node(data)
        if self.head is None:
            self.head = new_element
            self.head.next = self.head
            return
        # for (int current=self.head)

    def print_list(self):
        current = self.head
        while True:
            print(str(self.head.data) + "->")
            current = current.next
            if current is self.head:
                break


ll = CircularLinkedList()
ll.insert_at_beginning(10)
ll.print_list()
