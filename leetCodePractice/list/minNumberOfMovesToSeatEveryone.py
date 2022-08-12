class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        
        total = 0
        for i in range(len(seats)):
            studentNum = students[i]
            seatNum = seats[i]
            total += abs(studentNum - seatNum)
            
        return total
            