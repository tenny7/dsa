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

    def delete_first(self):
        if self.head is None:
            return None
        current = self.head
        temp = current.next
        current.next = None
        self.head = temp
        return self.head

    def delete_last_node(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return None

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        return self.head

    def insert_at_position(self, position, value):
        counter = 1
        new_element = Node(value)
        if self.head is None:
            self.head = new_element
            return

        current = self.head

        if current is None:
            return self.head

        while current.next is not None:
            if counter == position - 1:
                new_element.next = current.next
                current.next = new_element
                return
            counter += 1
            current = current.next
        return "position and value not set"

    def search_position_element(self, element):
        current = self.head
        counter = 1
        while current is not None:
            if current.data == element:
                print(counter)
                return 
            current = current.next
            counter += 1
        print(-1)




ll = LinkedList()

ll.insert_at_beginning(10)
# lambda x: print(2+3)

ll.insert_at_beginning(11)
ll.insert_at_beginning(5)
ll.insert_at_beginning(13)
ll.insert_at_beginning(16)
ll.insert_at_beginning(17)
ll.insert_at_beginning(143)

# ll.insert_at_position(9, 88)
ll.search_position_element(16)
# ll.insert_at_position(2, 48)
# ll.insert_at_position(9, 1067)
# ll.delete_first()
# ll.delete_last_node()
# ll.print_recursive(13)
ll.print_list()
