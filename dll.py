class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = self.prev = None


class DoubleLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        new_element = Node(data)
        if self.head is None:
            self.head = new_element
            return self.head
        tmp = self.head
        new_element.next = tmp
        tmp.prev = new_element
        self.head = new_element

    def print_dll(self):
        if self.head is None:
            return
        current = self.head
        result = ''
        while current is not None:
            result += str(current.data) + '->'
            current = current.next
        print(result)

    # def reversed_dll(self):
    #     if self.head is None:
    #         return None
    #     if self.head.next is None:
    #         return None
    #     current = self.head
    #     while current.next is not None:
    #         current.next = current.next.prev
    #         current.next.prev = current.next
    #         current = current.prev


dll = DoubleLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_beginning(30)
dll.insert_at_beginning(40)
dll.reversed_dll()
dll.print_dll()
