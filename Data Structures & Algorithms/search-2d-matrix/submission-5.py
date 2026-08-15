class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        arr = 0
        while l <= r:
            mid = (l + r) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid]) - 1]:
                arr = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        array = matrix[arr]
        l, r = 0, len(array) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > array[mid]:
                l = mid + 1
            elif target < array[mid]:
                r = mid - 1
            else:
                return True
            
        return False

        