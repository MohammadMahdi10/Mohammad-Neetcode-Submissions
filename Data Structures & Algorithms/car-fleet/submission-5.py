class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distances = [0] * len(position)

        for i, n in enumerate(position):
            distances[i] = target - n
        
        stack = []
        pairs = list(zip(distances, speed)) 
        pairs.sort()

        for i, n in enumerate(pairs):
            time = n[0] / n[1]
            if stack and time <= (stack[-1][0] / stack[-1][1]):
                continue
            stack.append((n[0], n[1]))
        
        return len(stack)
