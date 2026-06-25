class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        mid = 0
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for b in piles:
                if b <= mid:
                    total += 1
                elif b % mid == 0:
                    total += b // mid
                elif b > mid:
                    total += (b // mid) + 1
            print(total)
            if total <= h:
                r = mid
            l = mid + 1
            #else:
            #    l = mid + 1                
                    
        return mid