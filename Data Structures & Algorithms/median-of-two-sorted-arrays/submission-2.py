class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            B, A = nums1, nums2
        
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2

        while True:
            midA = (l + r) // 2
            midB = half - midA - 2

            aLeft = A[midA] if midA >= 0 else float("-inf")
            aRight = A[midA + 1] if midA + 1 < len(A) else float("inf")
            bLeft = B[midB] if midB >= 0 else float("-inf")
            bRight = B[midB + 1] if midB + 1 < len(B) else float("inf")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 == 0:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
                else:
                    return min(aRight, bRight)
            elif aLeft > bRight:
                r = midA - 1
            else:
                l = midA + 1
