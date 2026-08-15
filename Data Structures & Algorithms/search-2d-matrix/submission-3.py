class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        


        for m in matrix:
            l, r = 0, len(m) - 1
            while l <= r:
                mid = (l + r) // 2
                if target > m[mid]:
                    l = mid + 1
                elif target < m[mid]:
                    r = mid - 1
                else:
                    return True
            
            return False

        