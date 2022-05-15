class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        black = "aceg"
        white = "bdfh"
        
        if coordinates[0] in black:
            return int(coordinates[1]) % 2 == 0
        else:
            return int(coordinates[1]) % 2 != 0
            
        