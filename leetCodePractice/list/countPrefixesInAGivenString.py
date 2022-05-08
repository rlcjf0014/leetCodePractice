class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        output = 0
        
        for letter in words:
            if letter[0] == s[0]:
                if letter in s[:len(letter)]:
                    output +=1
        
        return output