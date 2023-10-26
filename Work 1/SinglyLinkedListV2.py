from Node import Node

class SinglyLinkedListV2:
    COUNT_APPEND, COUNT_REMOVE = 0, 0
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node  # Link the new node after the current tail
            self.tail = new_node      # Update the tail to the new node
        else:
            self.head = new_node     # If the list is empty, both head and tail are the new node
            self.tail = new_node
        self.COUNT_APPEND += 1
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError('Empty List')
        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            last_node = self.__get_node(self.size - 2)
            last_node.next = None
            self.tail = last_node  # Update the tail to the new last node
        self.size -= 1
    
    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError(f"Index must be within the range [0, {self.size - 1}]")
        
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size == 0:
                self.tail = new_node  # If the list was empty, the new node is also the tail
        elif index == self.size:
            self.tail.next = new_node  # Inserting at the end
            self.tail = new_node      # Update the tail to the new node
        else:
            previous = self.__get_node(index - 1)
            new_node.next = previous.next
            previous.next = new_node
        self.size += 1
    
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be within the range [0, {self.size-1}]")

        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None  # If removing the last element, update the tail
            self.COUNT_REMOVE += 1
        else:
            previous = self.__get_node(index - 1)
            previous.next = previous.next.next
            if index == self.size - 1:
                self.tail = previous  # If removing the last element, update the tail
        self.size -= 1
    
    def find(self, data):
        current = self.head
        index = 0

        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1
        
    
    def __get_node(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"Index must be within the range [0, {self.size-1}]")

        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def __getitem__(self, index):
        node = self.__get_node(index)
        return node.data if node else None
        
    def __setitem__(self, index, data):
        node = self.__get_node(index)
        if node:
            node.data = data
        else:
            raise IndexError(f"Index must be within the range [0, {self.size-1}]")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self.size
    

if __name__ == "__main__":
    a = SinglyLinkedListV2()

    a.append(0)
    a.append(1)
    a.append(2)
    a.insert(0, 10)
    a.pop()
    a.insert(2, 3)

    print(a.find(1))

    print(a[0], a[1], a[2], a[3])