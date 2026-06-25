class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        answer = r
        while l <= r:
            mid = (l + r) // 2
            total = 0
            for b in piles:
                total += math.ceil(b / mid)
            if total <= h:
                r = mid - 1
                answer = min(answer, mid)
            else:
                l = mid + 1             
                    
        return answer