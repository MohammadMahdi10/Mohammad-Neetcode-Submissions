class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        # loop through one each value and pointer each value from i+1 to end of array
        # while l<r

        contains = []
        nums = sorted(nums)
        # [-4, -1, -1, 0, 1, 2]
        
        for i, n in enumerate(nums):
            if n == nums[i-1] and i > 0:
                continue

            l, r = i+1, len(nums)-1

            while l<r:
                sums = n + nums[l] + nums[r]

                if sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1
                else:
                    contains.append([n, nums[l], nums[r]])
                    l += 1
        
        return contains
