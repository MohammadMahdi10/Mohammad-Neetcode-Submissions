class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6] : 7
        # we do difference 4, 3, 2, 1 and store in hash map (key is diff and val is index)

        contains = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in contains:
                return [contains[difference], i]
            contains[n] = i
