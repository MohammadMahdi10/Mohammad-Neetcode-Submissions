class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # minimise heights and then find greatest minimum heights than spans all bars
        # mulitply by width for all of them

        # redo this

        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            current = i
            while stack and h < stack[-1][1]:
                val = stack.pop()
                area = val[1] * (i - val[0])
                current = val[0]
                maxArea = max(maxArea, area)

            stack.append((current, h))
        
        for height in stack:
            area = height[1] * (len(heights) - height[0])
            maxArea = max(maxArea, area)

        return maxArea


