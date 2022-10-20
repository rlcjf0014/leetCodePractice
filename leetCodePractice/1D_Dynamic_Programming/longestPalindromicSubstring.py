class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            # abba
            p1 = self.makePalindrome(s, i, i+1)
            # aba
            p2 = self.makePalindrome(s, i, i)
            # get maximum
            result = max([result, p1, p2], key=lambda x: len(x))
        return result

        

    def makePalindrome(self, target, f, l):
        while f >= 0 and l < len(target) and target[f] == target[l]:
            f -= 1
            l += 1
        return target[f+1:l]
