class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        
        record = {}
        for letter in s:
            if letter in record:
                record[letter] += 1
            else:
                record[letter] = 1
        
        letterVal = record.values()
        length = 0
        hasOdd = False
        for val in letterVal:
            if val % 2 == 0:
                length += val
            else:
                newNum = val - 1
                length += newNum
                if hasOdd is False:
                    hasOdd = True
        return length + 1 if hasOdd is True else length