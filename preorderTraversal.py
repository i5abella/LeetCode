# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root == None:
            return []
            
        stack = [root]
        result = []
        while stack:
            temp = stack.pop()
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
            result.append(temp.val)
        return result
