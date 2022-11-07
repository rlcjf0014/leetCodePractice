class Solution:
    def maximum69Number (self, num: int) -> int:
        strNum = str(num)
        for i in range(len(strNum)):
            if strNum[i] == "6":
                return int(strNum[:i] + "9" + strNum[i+1:])

        return num
