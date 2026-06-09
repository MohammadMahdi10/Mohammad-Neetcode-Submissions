class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        change = [0 for _ in range(len(temperatures))]

        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                stackValue, stackIndex  = stack.pop()
                change[stackIndex] = i - stackIndex
            stack.append([n, i])
        
        return change