class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for letter in columnTitle:
            difference = ord(letter) - ord('A') + 1
            result = result * 26 + difference
        return result