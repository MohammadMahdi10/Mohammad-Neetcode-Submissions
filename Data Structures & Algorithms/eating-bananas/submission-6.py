class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        k = float("infinity")
        while l <= r:
            mid = (l+r) // 2

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            print(mid, hours)
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
                k = min(k, mid)
        
        return k
