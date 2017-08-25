class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return math.sqrt(n)
        # bulbs = []
        # for i in range(n):
        #     bulbs.append(0)
        # for i in range(1, n+1):
        #     for b in range(len(bulbs)):
        #         if (b+1) % i == 0:
        #             bulbs[b] += 1
        # on = 0
        # for b in bulbs:
        #     if b % 2 != 0:
        #         on += 1
        # return on
