class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        output = 0
        g.sort()
        s.sort()
        for num in g:
            # print(num)
            for i in range(len(s)):
                if s[i] >= num:
                    output += 1
                    s.remove(s[i])
                    break
            
        return output