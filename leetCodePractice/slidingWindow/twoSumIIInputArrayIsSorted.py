class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # record = {}
        # for i in range(len(numbers)):
        #     want = target - numbers[i]
        #     if want in record:
        #         return [record[want] + 1, i + 1]
        #     else:
        #         record[numbers[i]] = i

        l = 0
        r = len(numbers) - 1

        while l != r:
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            elif (numbers[l] + numbers[r]) < target:
                l += 1
            else:
                return [l+1, r+1]
    

        

        