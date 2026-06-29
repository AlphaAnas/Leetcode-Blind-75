

'''


'''


from typing import List



def isValidSudoku( board: List[List[str]]) -> bool:


    # check row
   
    for r in range(len(board)):
        row_set = set()
        for c in range(len(board)):
            curr = board[r][c]
            if curr == ".": 
                continue
            if curr in row_set:
                return False
            row_set.add(curr)
            
    # rows cleared uptill here

    # check cols
    for c in range(len(board)):
        col_set = set()
        for r in range(len(board)):
            curr = board[r][c]
            if curr == ".":  
                continue
            if curr in col_set:
                return False
            col_set.add(curr)
    # cols clear uptill now

    # check 3x3 boxes now!
    for sq in range(0, len(board)):
        r_c_set = set()
        for r in range(3):
            for c in range(3):
                row_no = (sq // 3) * 3 + r
                col_no = (sq // 3) * 3 + c

                curr = board[row_no][col_no]
                if curr == ".":
                    continue
                if curr in r_c_set:
                    return False
                r_c_set.add(curr)
    


    return True



board = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
board = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","1",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
