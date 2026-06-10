class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we need to find the time to consider the car in a fleet
        # else, its a part of its own fleet
        # stack is needed to hold unique fleets
        # if current pos < pos in front and speed > pos in front, they become a fleet

        actualPos = []
        stack = []

        for n, s in zip(position, speed):
            actualPos.append((n, s))

        actualPos = sorted(actualPos, reverse=True)
        
        # t=12
        # 10 2 1
        # 8 4 1
        # 5 1 7
        # 3 3 3
        # 0 1 12

        for n, s in actualPos:
            stack.append((n, s))
            if len(stack) == 1:
                continue
            else:
                if ((target - n) // s) <= ((target - stack[-2][0]) / stack[-2][1]):
                    stack.pop()
        
        return len(stack)
        


        # t=10
        # 4 2 3
        # 1 3 3



