class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        answer = 0
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
            if total <= h:
                r = mid - 1
                answer = mid
            else:
                l = mid + 1             
                    
        return answer