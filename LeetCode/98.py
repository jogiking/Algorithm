# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        핵심 아이디어: 중위순회를 한 다음, 오름차순인지 확인한다
        """
        
        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            arr.append(root.val)
            inOrder(root.right)
        
        arr = []
        inOrder(root)
        
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True