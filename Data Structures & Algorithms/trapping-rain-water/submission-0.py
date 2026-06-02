class Solution:
    def trap(self, height: List[int]) -> int:
        # from video

        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        
        count = 0

        while l < r:
            if maxR < maxL:
                r -= 1

                val = maxR - height[r]
                if val > 0:
                    count += val
                
                if height[r] > maxR:
                    maxR = height[r]
            else:
                l += 1
                
                val = maxL - height[l]
                if val > 0:
                    count += val
                
                if height[l] > maxL:
                    maxL = height[l]
        
        return count


