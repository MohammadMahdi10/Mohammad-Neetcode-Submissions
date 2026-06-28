class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]

        total = 1
        for i, n in enumerate(nums):
            res[i] = total
            total = total * nums[i]

        total = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= total
            total = total * nums[i]
        
        return res
