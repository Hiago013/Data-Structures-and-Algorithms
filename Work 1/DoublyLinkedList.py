from DoublyNode import DoublyNode

class DoublyLinkedList:
    COUNT_APPEND, COUNT_REMOVE = 0, 0
    def __init__(self):
        self.size = 0
        self.head = DoublyNode(None)  # Create a head node with None data
        self.tail = self.head  # Initially, both head and tail point to the head node
    
    def append(self, data):
        new_node = DoublyNode(data)
        new_node.prev = self.tail
        self.tail.next = new_node  # Link the new node after the current tail
        self.tail = new_node      # Update the tail to the new node
        self.size += 1
        self.COUNT_APPEND += 1
    
    def pop(self):
        if self.size == 0:
            raise ValueError('Empty List')

        last_node = self.tail
        self.tail = last_node.prev
        self.tail.next = None
        self.size -= 1
    
    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError(f"Index must be within the range [0, {self.size}]")
        
        new_node = DoublyNode(data)
        current = self.__get_node(index - 1)

        new_node.next = current.next
        new_node.prev = current
        current.next = new_node

        if index == self.size:
            self.tail = new_node  # If inserting at the end, update the tail
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be within the range [0, {self.size-1}]")

        self.COUNT_REMOVE += 1
        current = self.__get_node(index)

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next  # Update the head if removing the first element

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev  # Update the tail if removing the last element

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

    def __get_node(self, index):
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
    a = DoublyLinkedList()