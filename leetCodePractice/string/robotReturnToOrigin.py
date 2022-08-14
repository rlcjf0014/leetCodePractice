class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        robot = [0, 0]
        for move in moves:
            if move == "R":
                robot[0] += 1
            elif move == "L":
                robot[0] -= 1
            elif move == "U":
                robot[1] += 1
            else:
                robot[1] -= 1
        return True if robot[0] == 0 and robot[1] == 0 else False
        