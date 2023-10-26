class StaticList:
    COUNT_APPEND, COUNT_REMOVE = 0, 0
    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self.size = 0
        self.values = [None] * max_size  # Use a Python list to store values

    def append(self, data):
        self.COUNT_APPEND += 1
        if not self.is_full():
            self.values[self.size] = data
            self.size += 1
        else:
            raise IndexError("Full list")

    def pop(self):
        if not self.is_empty():
            self.size -= 1
        else:
            raise IndexError("Empty list")

    def insert(self, index, data):
        if not self.is_full() and 0 <= index < self.size:
            for i in range(self.size, index, -1):
                self.values[i] = self.values[i - 1]
            self.values[index] = data
            self.size += 1
        else:
            raise IndexError("Sequence index out of range")

    def remove(self, index):
        if not self.is_empty() and 0 <= index < self.size:
            for i in range(index, self.size - 1):
                self.values[i] = self.values[i + 1]
                self.COUNT_REMOVE += 1
            self.size -= 1
        else:
            raise IndexError("Sequence index out of range")

    def find(self, elem):
        for i in range(self.size):
            if self.values[i] == elem:
                return i
        return -1  # Return -1 if the element is not found

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.values[index]
        else:
            raise IndexError("Sequence index out of range.")
        
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self.size

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0
    
    def __repr__(self):
        count = 0
        r = ""
        while(count < self.size):
            r = r + str(self.values[count]) + "->"
            count += 1
        return r

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    a = StaticList()

    a.append(0)
    a.append(1)
    a.append(2)
    a.remove(1)
    a.insert(1, 10)


    print(str(a))