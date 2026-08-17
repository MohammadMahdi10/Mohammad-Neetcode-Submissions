class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float("infinity")
        val = 0

        while l <= r:
            mid = (l + r) // 2
            sums = 0
            for n in piles:
                if n <= mid:
                    sums += 1
                else:
                    rem = n % mid
                    div = n // mid
                    sums += rem + div

            if sums <= h:
                val = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return val