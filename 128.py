class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        d = dict()
        for n in nums:
            left = 0 
            right = 0
            if n not in d:
                if n-1 in d:
                    left = d[n-1]
                if n+1 in d:
                    right = d[n+1]
                total = left + right + 1
                d[n] = total
                
                res = max(res, total)
                d[n-left] = total
                d[n+right] = total
        return res
