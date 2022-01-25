class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        mountain = 0
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                mountain += 1
            elif arr[i-1] == arr[i]:
                return False
        
        if mountain == 1 and arr[-1] < arr[-2] and arr[0] < arr[1]:
            return True
        return False
    
            
            