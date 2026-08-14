class TimeMap:
    def __init__(self):
        self.contains = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.contains:
            self.contains[key] = []
        self.contains[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        arr = self.contains[key]
        target = timestamp
        l, r = 0, len(arr)

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][1] <= target:
                return arr[mid][0]
            elif arr[mid][1] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return ""