# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def doTraverse(self, root, result):
        if not root:
            return
        result.append(root.val)
        self.doTraverse(root.left, result)
        self.doTraverse(root.right, result)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.doTraverse(root, result)
        return result

        
