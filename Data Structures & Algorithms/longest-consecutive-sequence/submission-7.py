# redo this later
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # get value minimum for that sequence
        # check if n+1 exists and if so, increment count
        # if sequence broken, store count in biggest
        # then go to next number and check if minimum again
        # same procedure
        # return biggest

        contains = set()
        biggest = 0

        for n in nums:
            contains.add(n)

        for n in nums:
            if n-1 not in contains:
                val = 0
                while (n+val) in contains:
                    val += 1
                if val > biggest:
                    biggest = val

        return biggest       

