class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        biggest = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = height * width

            if area > biggest:
                biggest = area
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return biggest