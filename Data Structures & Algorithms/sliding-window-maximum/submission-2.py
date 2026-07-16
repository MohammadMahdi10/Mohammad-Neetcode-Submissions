class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        queue = []

        for r in range(len(nums)):
            if (r - l + 1) < k:
                while queue and nums[r] > queue[-1]:
                    queue.pop()
                queue.append(nums[r])
            else:
                while queue and nums[r] > queue[-1]:
                    queue.pop()
                queue.append(nums[r])
                res.append(queue[0])

                l += 1

        return res