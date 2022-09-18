class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        
        def convertToNum(word):
            result = ""
            for letter in word:
                num = ord(letter) - 97
                result += str(num)
            return result
        
        
        sumTwo = int(convertToNum(firstWord)) + int(convertToNum(secondWord))
        
        return True if sumTwo == int(convertToNum(targetWord)) else False