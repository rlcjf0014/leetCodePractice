class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        
        i = 0
        temp = 0
        maxLen = 0
        curr = None
        while i < len(s):
            if curr is None:
                curr = s[i]
                temp += 1
            else:
                if s[i] == curr:
                    temp += 1
                else:
                    if temp > maxLen:
                        maxLen = temp
                    curr = s[i]
                    temp = 1
            i+=1
            
        if temp > maxLen:
            maxLen = temp
            
        return maxLen