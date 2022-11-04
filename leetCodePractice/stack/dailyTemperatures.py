class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait = [0]*len(temperatures)
        stack = []
        
        for i, x in enumerate(temperatures):     
            while stack and x > temperatures[stack[-1]]:
                j = stack.pop()
                wait[j] = i - j
            stack.append(i)
        
        return wait

            