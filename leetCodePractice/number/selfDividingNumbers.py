class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            stringNum = str(i)
            if "0" in stringNum:
                continue
            else:
                check = True
                for digit in stringNum:
                    if i % int(digit) != 0:
                        check = False
                        break
                if check:
                    result.append(i)
            
        return result