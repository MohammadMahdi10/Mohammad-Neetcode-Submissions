class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[l] > nums[r]:
                l = mid + 1
                res = min(nums[l], res)
            else:
                r = mid - 1
                res = min(nums[r], res)
        
        return res