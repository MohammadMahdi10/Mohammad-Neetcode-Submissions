class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = nums[l]
        while l <= r:
            mid = (l + r) // 2
            res = min(nums[l], res)
            if nums[l] > nums[mid]:
                r = mid - 1
                res = min(nums[mid], res)
            else:
                l = mid + 1
                res = min(nums[mid], res)
        
        return res