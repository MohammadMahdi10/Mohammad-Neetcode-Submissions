class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        val = float("infinity")

        while l <= r:
            mid = (l + r) // 2

            sums = 0
            for n in piles:
                if n <= mid:
                    sums += 1
                else:
                    div = n // mid
                    sums += div + 1

            if sums <= h:
                val = min(val, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return val