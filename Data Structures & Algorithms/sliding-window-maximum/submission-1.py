class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force way

        res = []
        l = 0
        maxVal = 0

        for r in range(len(nums)):
            maxVal = max(maxVal, nums[r])
            if r - l + 1 == k:
                l += 1
                res.append(maxVal)
        
        return res