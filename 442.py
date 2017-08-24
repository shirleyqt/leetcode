class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        result = []
        for n in d:
            if d[n] == 2:
                result.append(n)
        return result
