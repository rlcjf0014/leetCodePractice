class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """        
        i = len(s) - 1
        j = len(t) - 1
        
        while i > -1 and j > -1:
            if s[i] == t[j]:
                i -= 1
                j -=1
            else:
                j -= 1
        if i == -1:
            return True
        else:
            return False
        
        