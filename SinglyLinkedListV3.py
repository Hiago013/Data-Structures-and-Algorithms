from Node import Node

class SinglyLinkedListV3:
    COUNT_APPEND, COUNT_REMOVE = 0, 0
    def __init__(self):
        self.size = 0
        self.head = Node(None)  # Create a head node with None data
        self.tail = self.head  # Initially, both head and tail point to the head node
    

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node  # Link the new node after the current tail
        self.tail = new_node      # Update the tail to the new node
        self.size += 1
        self.COUNT_APPEND += 1

    def pop(self):
        if self.size == 0:
            raise ValueError('Empty List')

        current = self.__get_node(self.size - 2)  # Get the second-to-last node
        current.next = None
        self.tail = current  # Update the tail to the new last node
        self.size -= 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError(f"Index must be within the range [0, {self.size - 1}]")
        
        new_node = Node(data)
        current = self.__get_node(index - 1)

        new_node.next = current.next
        current.next = new_node

        if index == self.size:
            self.tail = new_node  # If inserting at the end, update the tail
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be within the range [0, {self.size-1}]")

        self.COUNT_REMOVE += 1
        current = self.__get_node(index - 1)

        current.next = current.next.next

        if index == self.size - 1:
            self.tail = current  # If removing the last element, update the tail
        self.size -= 1

    def find(self, data):
        current = self.head.next  # Start from the node after the head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1

    def __get_node(self, index) -> Node: 
        if index < -1 or index >= self.size:
            raise IndexError(f"Index must be within the range [0, {self.size-1}]")

        current = self.head
        for _ in range(index + 1):  # Start from the head and iterate to the desired node
            current = current.next
        return current

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be within the range [0, {self.size-1}]")

        node = self.__get_node(index)
        return node.data

    def __setitem__(self, index, data):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be within the range [0, {self.size-1}]")

        node = self.__get_node(index)
        node.data = data

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self.size

if __name__ == "__main__":
    a = SinglyLinkedListV3()

    a.append(0)
    a.append(1)
    a.append(2)
    a.insert(0, 10)
    a.pop()
    a.insert(2, 3)

    print(a.find(1))

    print(a[0], a[1], a[2], a[3])