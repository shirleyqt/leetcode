### [Easy][119] Pascal's Triangle II ###

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        res = [[1], [1,1]]
        for i in range(2, rowIndex+1):
            new = [1]
            for j in range(len(res[i-1])-1):
                new.append(res[i-1][j]+res[i-1][j+1])
            new.append(1)
            res.append(new)
        return res[-1]
