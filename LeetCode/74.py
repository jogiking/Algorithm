class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h,w = len(matrix),len(matrix[0])
        left = 0
        right = h-1
        
        while left<right:
            mid = (left+right)//2
            if matrix[mid][-1]<target:
                left = mid+1
            elif matrix[mid][-1]>target:
                right = mid
            else:
                return True
        
        i = right
        left = 0
        right = w-1
        while left<right:
            mid = (left+right)//2
            if matrix[i][mid]<target:
                left = mid+1
            elif matrix[i][mid]>target:
                right = mid-1
            else:
                return True
        return True if matrix[i][right]==target else False
        
                
