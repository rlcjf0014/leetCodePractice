class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        allCapital = word.isupper()
        firstCapital = word[0].isupper()
        allLower = word.islower()
        
        for letter in word[1:]:
            if letter.isupper():
                firstCapital = False
                break
        
        return allCapital or firstCapital or allLower
        