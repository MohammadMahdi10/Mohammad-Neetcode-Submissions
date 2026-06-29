class TimeMap:
    def __init__(self):
        self.timeMap = {} # timestamp : {key : value}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([value, timestamp])
        else:
            self.timeMap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if len(self.timeMap) == 0:
            return ""

        prev = None
        if key in self.timeMap:
            for t in range(len(self.timeMap[key])):
                prev = t-1
                if self.timeMap[key][t][1] == timestamp:
                    return self.timeMap[key][t][0]
                

            
        return self.timeMap[key][prev][0]