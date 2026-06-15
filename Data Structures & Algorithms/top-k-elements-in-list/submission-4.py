class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        contains = {}
        bucket = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            contains[n] = contains.get(n, 0) + 1
        
        for v, f in contains.items():
            bucket[f].append(v)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result
                