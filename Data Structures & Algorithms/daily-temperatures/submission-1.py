class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # recap

        res = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, n)) 
        
        return res