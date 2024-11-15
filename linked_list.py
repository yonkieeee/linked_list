class Node:
    def __init__(self, value):
        if not isinstance(value, (int, float, str)):
            raise TypeError("Type Error")
        self.previus = None
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, array=[]):
        self.head = None
        self.size = 0

    def append(self, value):
        if str(value).isdigit():
            new_node = Node(float(value))
        else:
            new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.previus = current

        self.size += 1

    def __len__(self):
        return self.size

    def find(self, num):
        if self.head is None:
            raise ValueError("ValueError")

        current = self.head

        while current is not None:
            if current.value == num:
                return current
            current = current.next

        raise ValueError(f"ValueError")

    def get(self, index):
        if self.head is None:
            raise IndexError("Index error")
        elif index >= self.size or index < 0:
            raise IndexError("Index error")
        current = self.head

        for _ in range(index):
            current = current.next

        return current


    def remove(self, value):
        if self.head is None:
            raise ValueError("ValueError")

        current = self.find(value)

        if current == self.head:
            self.head = self.head.next
            if self.head:
                self.head.previus = None
        elif current.next is None:
            if current.previus:
                current.previus.next = None

        else:
            if current.previus:
                current.previus.next = current.next
            if current.next:
                current.next.previus = current.previus

        self.size -= 1
        del current

    def insert(self, value, index):
        if index > self.size or index < 0:
            raise IndexError("Index error")

        new_node = Node(value)

        if index == self.size:
            self.append(value)
            return
        elif index == 0:
            new_node.next = self.head
            self.head.previus = new_node
            self.head = new_node
        else:
            current = self.get(index)
            prev_node = current.previus

            prev_node.next = new_node
            new_node.previus = prev_node
            new_node.next = current
            current.previus = new_node

        self.size += 1

    def __str__(self):
        current = self.head
        list = []

        while current is not None:
            if isinstance(current.value, str):
                list.append(repr(current.value))
            else:
                list.append(str(current.value))
            current = current.next

        return f"[{', '.join(list)}]"

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
