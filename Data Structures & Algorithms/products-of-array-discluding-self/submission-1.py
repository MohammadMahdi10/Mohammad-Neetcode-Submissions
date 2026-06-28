class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]

        prefix, total = [0 for _ in range(len(nums))], 1
        for i, n in enumerate(nums):
            if i == 0:
                prefix[i] = 1
                continue
            total = total * nums[i-1]
            prefix[i] = total

        suffix, total = [0 for _ in range(len(nums))], 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix[i] = 1
                continue
            total = total * nums[i+1]
            suffix[i] = total
        
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        
        return res
