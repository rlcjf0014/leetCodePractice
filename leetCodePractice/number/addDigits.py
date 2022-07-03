class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        strNum = str(num)
        while len(strNum) != 1:
            sumNum = 0
            for digit in strNum:
                sumNum += int(digit)
            strNum = str(sumNum)
        return int(strNum)
            