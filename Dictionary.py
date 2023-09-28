from Queue import Queue
class Dictionary:
    # A dictionary to map version names to their respective queue implementations
    SUPPORTED_VERSIONS = {
        0 : 'static',
        1 : 'singlylinkedlist',
        2 : 'singlylinkedlistv2',
        3 : 'singlylinkedlistv3',
        4 : 'doublylinkedlist'
    }
    def __init__(self, version=0):
        selected_version = self.SUPPORTED_VERSIONS.get(version, 'static')
        self._keys = Queue(selected_version)
        self._values = Queue(selected_version)
        self.size = 0

    def insert(self, key, value):
        self._keys.push(key)
        self._values.push(value)
        self.size += 1

    def pop(self):
        self._keys.pop()
        self._values.pop()
        self.size -= 1

    def get(self, key):
        current_key = None
        current_value = None

        for _ in range(self.size):
            current_key = self._keys.pop()
            current_value = self._values.pop()

            self._keys.push(current_key)
            self._values.push(current_value)


            if current_key == key:
                return current_value

        raise KeyError(f"Key '{key}' not found in the dictionary")
    
    def clean(self):
        while self.size != 0:
            self.pop()
    
    def get_basic_operation(self):
        return self._keys.queue.COUNT_APPEND + self._keys.queue.COUNT_REMOVE

    def reset_counters(self):
        self._keys.queue.COUNT_APPEND = 0
        self._keys.queue.COUNT_REMOVE = 0

if __name__ == '__main__':
    a = Dictionary(0)
    [a.insert(i, 10) for i in range(100)]
    a.get(99)
