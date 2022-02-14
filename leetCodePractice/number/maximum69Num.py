class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        newStr = str(num)
        result = ""
        for i in range(len(newStr)):
            if newStr[i] == "6":
                print(i)
                result = newStr[:i] + "9" + newStr[i+1:]
                break
        return int(result) if result != "" else num