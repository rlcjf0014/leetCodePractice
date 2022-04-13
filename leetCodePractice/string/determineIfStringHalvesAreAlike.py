class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        firstHalf = s[:len(s)/2]
        secondHalf = s[len(s)/2:]
        
        firstCount = 0
        secondCount = 0
        
        for i in range(len(firstHalf)):
            if firstHalf[i] in vowels:
                firstCount+=1
            if secondHalf[i] in vowels:
                secondCount+=1
        
        return firstCount == secondCount
        