class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = t
        for i in range(len(s)):
            result = result.replace(s[i], "", 1)
        return result
                
        