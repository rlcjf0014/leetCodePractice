class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        result = -1
        for i in range(len(s)):
            currLetter = s[i]
            if s[i] in record:
                minNum = record[currLetter]
                diff = abs(minNum - i) - 1
                result = max(result, diff)
            else:
                record[currLetter] = i
        
        return result