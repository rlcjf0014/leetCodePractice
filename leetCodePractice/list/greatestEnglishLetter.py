class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for letter in s:
            if letter.isupper():
                if letter.lower() in s:
                    result.append(letter)
            if letter.islower():
                if letter.upper() in s:
                    result.append(letter)
        return max(result).upper() if len(result) > 0 else ""