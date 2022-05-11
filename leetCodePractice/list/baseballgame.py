class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = []
        for element in ops:
            if element == "C":
                result.pop()
            elif element == "D":
                result.append(2*int(result[-1]))
            elif element == "+":
                result.append(int(result[-1]) + int(result[-2]))
            else:
                result.append(element)
        finalSum = 0
        for num in result:
            finalSum += int(num)
        return finalSum
        