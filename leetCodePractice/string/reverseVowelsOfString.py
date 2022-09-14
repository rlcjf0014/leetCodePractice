class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = "aeiou"
        record = []
        for letter in s:
            if letter.lower() in vowel:
                record.insert(0, letter)
        
        j = 0
        newS = ""
        for i in range(len(s)):
            if s[i].lower() in vowel:
                newS += record[j]
                j+=1
            else:
                newS += s[i]
        
        return newS
                
        
        
            