### [Medium][264] Ugly Number II ###

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        t2 = 0
        t3 = 0
        t5 = 0
        res = [1]
        for i in range(1, n):
            small = min(res[t2]*2, res[t3]*3, res[t5]*5)
            res.append(small)
            if res[t2]*2 == small:
                t2 += 1
            if res[t3]*3 == small:
                t3 += 1
            if res[t5]*5 == small:
                t5 += 1
        return res[n-1]
