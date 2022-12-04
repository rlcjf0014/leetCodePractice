class Solution:
    def countAsterisks(self, s: str) -> int:
        n = len(s)
        res = 0
        isPair = False
        
        for i in range(n):
            # if * is outside of a pair add to result
            if not isPair and s[i] == "*":
                res += 1
                
            # track "|" pair by boolean toggle
            if s[i] == "|":
                isPair = not isPair
                
        return res