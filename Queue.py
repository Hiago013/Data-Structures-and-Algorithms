from StaticList import StaticList
from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedListV2 import SinglyLinkedListV2
from SinglyLinkedListV3 import SinglyLinkedListV3
from DoublyLinkedList import DoublyLinkedList

class Queue:
    # A dictionary to map version names to their respective queue implementations
    SUPPORTED_VERSIONS = {
        'static': StaticList,
        'singlylinkedlist': SinglyLinkedList,
        'singlylinkedlistv2': SinglyLinkedListV2,
        'singlylinkedlistv3': SinglyLinkedListV3,
        'doublylinkedlist': DoublyLinkedList
    }

    def __init__(self, version='static', max_size=1000):
        # Check if the selected version is supported
        if version.lower() not in self.SUPPORTED_VERSIONS:
            raise NameError("Unsupported queue version.")

        self.max_size = max_size
        self.size = 0

        # Create the queue instance based on the selected version
        self.queue = self.SUPPORTED_VERSIONS[version.lower()]()

    def push(self, data):
        # Check if the queue size is within the maximum limit
        if self.size < self.max_size:
            self.queue.append(data)
            self.size += 1

    def pop(self):
        # Check if the queue is not empty
        if self.size > 0:
            data = self.queue[0]
            self.queue.remove(0)
            self.size -= 1
            return data

    def front(self):
        # Check if the queue is not empty
        if self.size > 0:
            return self.queue[0]

    def clean(self):
        while self.size != 0:
            self.pop()   

    def __len__(self):
        return self.size


if __name__ == "__main__":
    fila = Queue(version='SinglyLinkedListV3')
    fila.push(100)
    fila.push(200)
    fila.push(300)
    fila.push(400)
    fila.push(500)
    fila.push(600)
    fila.push(700)
    for i in range(7):
        print(fila.pop())




