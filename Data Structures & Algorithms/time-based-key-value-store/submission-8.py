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
        if key in self.timeMap:
            l, r = 0, len(self.timeMap[key]) - 1

            while l <= r:
                mid = (l + r) // 2
                if self.timeMap[key][mid][1] <= timestamp:
                    res = self.timeMap[key][mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
                
        return res