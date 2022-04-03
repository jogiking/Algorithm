# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dict = defaultdict(list)
        
        def dfs(root, depth):
            if not root:
                return
            
            dict[depth].append(root.val)
            
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
            
        dfs(root, 0)
        return list(map(lambda x: x[1], sorted(list(dict.items()))))
        
        