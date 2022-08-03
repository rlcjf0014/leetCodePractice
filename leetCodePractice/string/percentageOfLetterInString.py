class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        if len(s) == 0 or s.count(letter) == 0:
            return 0
        else:
            return int(math.floor(s.count(letter) / float(len(s)) * 100))