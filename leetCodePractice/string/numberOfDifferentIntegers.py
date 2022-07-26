class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        result = []
        i = 0
        while i < len(word):
            if word[i].isnumeric():
                number = word[i]
                for j in range(i+1, len(word)+1):
                    if j == len(word):
                        i = j
                        result.append(int(number))
                        break
                    if word[j].isnumeric():
                        number+=word[j]
                    else:
                        i = j
                        result.append(int(number))
                        break
                        
            i+=1
        return len(set(result))