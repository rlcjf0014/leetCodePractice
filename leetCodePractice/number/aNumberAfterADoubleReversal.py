class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        rev = str(num)[::-1]
        up = int(rev)
        return num == int(str(up)[::-1])