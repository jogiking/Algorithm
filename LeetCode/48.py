# Time: O(N), Space: O(1)
# 각 원소를 한번씩만 방문해서 이동하고 있으므로 O(N).

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for gap in range(n//2): # 껍질 깊이
            for i in range(n-2*gap-1): # 열번호
                
                # 1: matrix[gap][gap+i]
                # 2: matrix[gap+i][n-gap-1]
                # 3: matrix[n-gap-1][n-gap-1-i]
                # 4: matrix[n-gap-1-i][gap]
                temp = matrix[gap][gap+i] # temp = 1
                matrix[gap][gap+i] = matrix[n-gap-1-i][gap] # 4->1
                matrix[n-gap-1-i][gap] = matrix[n-gap-1][n-gap-1-i] # 3->4
                matrix[n-gap-1][n-gap-1-i] = matrix[gap+i][n-gap-1] # 2->3
                matrix[gap+i][n-gap-1] = temp # 1->2