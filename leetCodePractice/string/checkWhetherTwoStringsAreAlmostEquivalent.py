class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        record1 = {}
        keys1 = []
        
        for letter in word1:
            if letter in record1:
                record1[letter]+=1
            else:
                keys1.append(letter)
                record1[letter] = 1
        
        for letter2 in word2:
            if letter2 in record1 and letter2 in keys1:
                record1[letter2]-=1
            elif letter2 in record1 and letter2 not in keys1:
                record1[letter2] += 1 
            else:
                record1[letter2] = 1 
        
        values1 = record1.values()
        values = map(lambda x: abs(x), values1)
        values.sort(reverse=True)
        
        return False if abs(values[0]) > 3 else True
        