class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        i = 0
        while i != len(word):
            if word[i] != ch:
                i+=1
            else:
                break
        if i == len(word):
            return word
                
        prefix = word[0:i+1]
        return prefix[::-1] + word[i+1:]