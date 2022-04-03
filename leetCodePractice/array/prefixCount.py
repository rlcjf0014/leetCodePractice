class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        checkLen = len(pref)
        result = 0
        for i in range(len(words)):
            temp = words[i][0:checkLen]
            if temp == pref:
                result+=1
        return result