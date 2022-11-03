class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in board:
            temp = set()
            for num in row:
                if num == ".":
                    continue
                elif num in temp:
                    return False
                else:
                    temp.add(num)

        # check columm
        for i in range(0, 9, 1):
            temp = set()
            for j in range(0, 9, 1):
                curr = board[j][i]
                if curr == ".":
                    continue
                elif curr in temp:
                    return False
                else:
                    temp.add(curr)

        
        # check 3 x 3 grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = set()
                for l in range(i, i+3, 1):
                    for m in range(j, j+3, 1):
                        curr = board[l][m]
                        if curr == ".":
                            continue
                        elif curr in temp:
                            return False
                        else:
                            temp.add(curr)

        return True
        
