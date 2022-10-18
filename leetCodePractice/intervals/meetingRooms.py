class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        meetingTime = 0
        intervals.sort(key = lambda x: x[0])

        for i in range(len(intervals)-1):
            currT = intervals[i]
            nextT = intervals[i+1]
            if currT[0] == nextT[0]:
                return False
            if nextT[1] <= currT[1]:
                return False
            if nextT[0] < currT[1]:
                return False
            


        
        return True
        
        
        