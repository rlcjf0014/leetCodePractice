class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        if len(num) == 1:
            if num[0] == "1" or num[0] == "8" or num[0] == "0":
                return True
            else:
                return False

        i = 0
        j = len(num) - 1

        while i <= j:
            first = num[i]
            last = num[j]

            if first != "8" and first != "0" and first != "1" and first != "6" and first != "9" and first != "0":
                return False

            if last != "8" and last != "0" and last != "1" and last != "6" and last != "9" and last != "0":
                return False

            if first == "6" and last != "9":
                return False
            
            if first != "9" and last == "6":
                return False
            
            if first == "9" and last != "6":
                return False

            if first == "1" and last != "1":
                return False

            if first == "8" and last != "8":
                return False

            if first != "8" and last == "8":
                return False

            i+=1
            j-=1
                

        return True