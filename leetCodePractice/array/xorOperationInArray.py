class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for i in range(0, n):
            arr.append(start + 2 * i)
        
        temp = arr[0]
        for i in range(1, len(arr)):
            temp = temp ^ arr[i]

        return temp