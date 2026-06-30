class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)
            if mid % 2 == 0:
                return nums[mid // 2]
            else:
                mid = mid // 2
                return (nums[mid] + nums[mid + 1]) / 2