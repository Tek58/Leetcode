class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr,left, right):
            mid = left + (right - left) // 2
            if left <= right:
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    return binary_search(arr, mid + 1, right)
                else:
                    return binary_search(arr, left, mid - 1)
            else:
                return False
                
        for i in range(len(matrix)):
            if binary_search(matrix[i], 0, len(matrix[i])-1):
                return True
        return False