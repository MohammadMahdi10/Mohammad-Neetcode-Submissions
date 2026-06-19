class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force way

        maxList = []
        l = 0

        for r in range(k-1, len(nums)):
            maxVal = nums[l]
            for i in range(l, r+1):
                if nums[i] > maxVal:
                    maxVal = nums[i]
            maxList.append(maxVal)
            l += 1
        
        return maxList