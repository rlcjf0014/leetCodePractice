class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = 0
        if low % 2 == 1 or high % 2 == 1:
            result += 1

        return ((high - low) // 2) + result