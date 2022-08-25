class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        records = []
        for letter in s:
            if letter.isalpha():
                records.append(letter)
        reversedR = records[::-1]
        
        result = ""
        num = 0
        for i in range(len(s)):
            if s[i].isalpha():
                result += reversedR[num]
                num+=1
            else:
                result += s[i]

        return result