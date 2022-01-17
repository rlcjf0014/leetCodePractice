class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        s = [[a, 'a'], [b, 'b'], [c, 'c']]
        ans = []
        while True:
            s.sort()
            i = 1 if len(ans) >= 2 and ans[-2] == ans[-1] == s[2][1] else 2
            if s[i][0]:
                ans.append(s[i][1])
                s[i][0] -= 1
            else:
                break
        return ''.join(ans)
            
            
            
            
        
            
        