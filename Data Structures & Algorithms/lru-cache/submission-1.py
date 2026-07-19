class LRUCache:

    def __init__(self, capacity: int):
        self.list1 = []
        self.list2 = []
        self.capacity = capacity
        self.index = -1

    def get(self, key: int) -> int:
        if key in self.list1:
            self.index = self.list1.index(key)
            keyN = self.list1[self.index]
            valN = self.list2[self.index]

            self.list1.pop(self.index)
            self.list2.pop(self.index)
            self.list1.append(keyN)
            self.list2.append(valN)
            
            return self.list2[-1]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.list1) >= self.capacity:
            self.list1.pop(0)
            self.list2.pop(0)
            self.list1.append(key)
            self.list2.append(value)
        elif key in self.list1:
            index = self.list1.index(key)
            self.list2[index] = value
        else:
            self.list1.append(key)
            self.list2.append(value)
        print(self.list1, self.list2)