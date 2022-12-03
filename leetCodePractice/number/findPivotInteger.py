class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1

        first = 1
        firstSum = 1
        last = n
        lastSum = n

        while first < last:
            if firstSum < lastSum:
                first += 1
                firstSum += first
            else:
                last -= 1
                lastSum += last

        if firstSum == lastSum:
            return first
        else:
            return -1