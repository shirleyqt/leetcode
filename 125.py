class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = 0
        e = len(s)-1
        s = s.lower()
        while e > b:
            if (s[b].isalpha() or s[b].isnumeric()) and (s[e].isalpha() or s[e].isnumeric()):
                if s[b] != s[e]:
                    return False
                b += 1
                e -= 1
            else:
                if (s[b].isalpha() or s[b].isnumeric()) and not (s[e].isalpha() or s[e].isnumeric()):
                    e -= 1
                else:
                    b += 1
        return True
