

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

    box_dic = {}
    for r in range(9):

        for c in range(9):

            sq_no = (r // 3) * 3 + (c // 3)
            
            if box_dic.get(sq_no, -1) == -1:
                box_dic[sq_no] = set()
            
            curr = board[r][c]
            if curr == ".":
                continue
            if curr not in box_dic[sq_no]:
                box_dic[sq_no].add(curr)
            else: # wo pehle se hei mojood
                print(box_dic[sq_no])
                return False
            
 

    return True




board =       [[".",".",".",".","5",".",".","1","."],
               [".","4",".","3",".",".",".",".","."],
               [".",".",".",".",".","3",".",".","1"],
               ["8",".",".",".",".",".",".","2","."],
               [".",".","2",".","7",".",".",".","."],
               [".","1","5",".",".",".",".",".","."],
               [".",".",".",".",".","2",".",".","."],
               [".","2",".","9",".",".",".",".","."],
               [".",".","4",".",".",".",".",".","."]] 

print(isValidSudoku(board)) # output false
# board = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
# print(isValidSudoku(board))
# board = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","1",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
# print(isValidSudoku(board))
