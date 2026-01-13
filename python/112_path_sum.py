# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode], targetSum: int, sum: int) -> bool:
        if not root:
            return False
        sum += root.val
        if sum == targetSum and not root.left and not root.right:
            return True
        return self.traverse(root.left, targetSum, sum) or self.traverse(root.right, targetSum, sum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.traverse(root, targetSum, 0)
        
