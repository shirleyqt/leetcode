class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        d = {"]":"[",")":"(","}":"{"}
        stack = []
        for c in s:
            if c in d.values():
                stack.append(c)
            elif c in d:
                if len(stack) == 0 or stack.pop() != d[c]:
                    return False
        return len(stack) == 0
