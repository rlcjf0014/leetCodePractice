class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        record = {}
        for i in range(len(names)):
            record[heights[i]] = names[i]

        temp = list(record.keys())
        temp.sort(reverse=True)

        result = []
        for height in temp:
            result.append(record[height])

        return result