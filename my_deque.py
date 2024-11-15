from linked_list import LinkedList


class Deque(LinkedList):
    def __init__(self):
        super().__init__()

    def pop(self):
        if self.head is None:
            raise ValueError("Value error")

        if self.head.next is None:
            value = self.head.value
            self.head = None
            self.size -= 1
            return value

        current = self.head
        while current.next:
            current = current.next

        value = current.value
        current.previus.next = None  # Remove last node
        self.size -= 1
        return value

    def pop_left(self):
        if self.head is None:
            raise ValueError("Value error")

        current = self.head  # Corrected to reference the Node, not its value

        value = current.value

        if self.head.next is None:  # Only one node in the list
            self.head = None
        else:
            self.head = self.head.next
            self.head.previus = None

        self.size -= 1
        return value

    def append_left(self, value):
        super().insert(value, 0)

    def remove(self, *args, **kwargs):
        raise NotImplementedError("NotImplementedError")

    def insert(self, *args, **kwargs):
        raise NotImplementedError("NotImplementedError")

