# remember DFS in binary tree is be recursing left and then right nodes
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        ans = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        ans.left = mergeTrees(root1 and root1.left,root2 and root2.left)
        ans.right = mergeTrees(root1 and root1.right,root2 and root2.right)
        
        return ans 
