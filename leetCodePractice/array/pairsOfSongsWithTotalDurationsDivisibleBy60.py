class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        record = collections.defaultdict(int)
        result = 0

        for t in time:
            if t % 60 == 0:
                result += record[0]
            else:
                result += record[60 - t % 60]
            record[t%60] += 1

        return result
            

