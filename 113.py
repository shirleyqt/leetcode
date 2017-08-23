class Solution(object):
    def pathSum(self, root, sum): 
        if root == None:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack != []:
            curr = stack.pop()
            val = curr
            ls = curr
            if curr.left == None and curr.right == None and val == 0:
                res.append(ls)
            if curr.right != None:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left != None:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 
