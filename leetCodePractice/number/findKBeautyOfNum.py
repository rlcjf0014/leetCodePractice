class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        total = 0
        numStr = str(num)
        for i in range(len(numStr)):
            newNum = numStr[i:i+k]
            if int(newNum) and len(newNum) == k:
                if num % int(newNum) == 0:
                    total += 1
        return total
                