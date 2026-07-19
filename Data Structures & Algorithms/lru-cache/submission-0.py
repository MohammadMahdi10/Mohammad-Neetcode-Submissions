class LRUCache:

    def __init__(self, capacity: int):
        self.list1 = []
        self.list2 = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.list1:
            index = self.list1.index(key)
            return self.list2[index]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.list1) >= self.capacity:
            self.list1.pop(0)
            self.list2.pop(0)
        elif key in self.list1:
            index = self.list1.index(key)
            self.list2[index] = value
        else:
            self.list1.append(key)
            self.list2.append(value)