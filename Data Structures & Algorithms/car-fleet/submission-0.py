class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we need to find the time to consider the car in a fleet
        # else, its a part of its own fleet
        # stack is needed to hold unique fleets

        stack = []

        for p, s in zip(position, speed):
            time = (target - p) // s
            if time not in stack:
                stack.append(time)
        
        return len(stack)