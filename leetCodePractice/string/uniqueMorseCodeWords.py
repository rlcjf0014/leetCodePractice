class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dict = {}
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        diff = ord('a')
        for i in words:
            ans = ""
            for j in range(len(i)):
                ans+=morse[ord(i[j])-diff]
            dict[ans] = 1
        return len(dict)