class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r ** 2 > x:
            r = (r + x/r) / 2
        return r
