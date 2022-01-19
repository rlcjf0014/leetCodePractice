class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        record=[]
        visited=set()
        for char in s:
            if char in visited:
                continue
            else:
                freq=s.count(char)
                record.append(freq)
                visited.add(char)
        record.sort()
        minFreq=0
        for num in range(1,len(record)):
            while(record.count(record[num]) != 1 and record[num] != 0):
                record[num] -= 1
                minFreq+=1
        return minFreq