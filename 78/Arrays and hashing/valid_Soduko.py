'''You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
'''

def Sudoku(board):
    #a set(), only stored unique elements
    rows = [set() for _ in range(9)]       # what unique digits are in each row [ set(), set(), set(), set(), set(), set(), set(), set(), set() ]
    cols = [set() for _ in range(9)]       # what unique digits in each column
    boxes = [set() for _ in range(9)]      # what unique digits in each 3x3 sub-box

    for r in range(9):
        for c in range(9):
            val = board[r][c]# this is something like row 1, column 3.
            if val == ".":# Get the value at row r, column c
                continue # Skip if the cell is empty (represented by ".")

            # Check for duplicates
            if val in rows[r]:
                return False #rows[r] is a set that stores all the values seen so far in row r.
            if val in cols[c]:
                return False
            box_index = (r // 3) * 3 + (c // 3)
            if val in boxes[box_index]:
                return False

            # Record the value
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_index].add(val)

    return True

    
#Using set() helps easily check if a digit has already appeared (sets do not allow duplicates).
 







print(Sudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))