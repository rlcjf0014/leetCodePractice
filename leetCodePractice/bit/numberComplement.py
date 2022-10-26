class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        compare = ""
        for bit in binary:
            if bit == "1":
                compare += "0"
            else:
                compare += "1"

        return int(compare, 2)
