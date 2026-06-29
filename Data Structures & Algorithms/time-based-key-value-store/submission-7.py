class TimeMap:
    def __init__(self):
        self.timeMap = {} # timestamp : {key : value}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([value, timestamp])
        else:
            self.timeMap[key] = [[value, timestamp]]


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timeMap.get(key, [])
        
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0] # closest we have seen so far
                l = mid + 1
            else:
                r = mid - 1 # bigger is invalid so we dont assign
        
        return res
