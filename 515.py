# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        visiting = [root]
        while visiting != [] and root != None:
            max = float('-inf')
            for i in range(len(visiting)):
                node = visiting.pop(0)
                if node.val > max:
                    max = node.val
                if node.left != None:
                    visiting.append(node.left)
                if node.right != None:
                    visiting.append(node.right)
            res.append(max)
        return res
