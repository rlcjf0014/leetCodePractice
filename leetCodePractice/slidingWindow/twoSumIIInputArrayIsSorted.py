class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(numbers)):
            want = target - numbers[i]
            if want in record:
                return [record[want] + 1, i + 1]
            else:
                record[numbers[i]] = i

        