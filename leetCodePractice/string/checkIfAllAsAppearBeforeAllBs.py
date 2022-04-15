class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'a' not in s or 'b' not in s:
            return True
        
        indexA = s.index('a')
        indexB = s.index('b')
        
        for i in range(len(s)):
            if s[i] == 'a':
                indexA = i if i > indexA else indexA
            if s[i] == 'b':
                indexB = i if i > indexB else indexB
            if indexB < indexA:
                return False
        
        return True