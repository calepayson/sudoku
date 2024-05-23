# solver.py - A command-line sudoku solver!
class SudokuBoard:

    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def getState(self):
        print("Input each row left to right starting from the top row")
        print("If a box is empty input '0' (zero) or just hit return")
        for i in range(9):
            for j in range(9):
                while True:
                    val = input(f"Row {i+1}, Col {j+1}: ")
                    if val == '':
                        val = 0
                    
                    try:
                        val = int(val)
                        if 0 <= val <= 9:
                            self.setCell(i, j, val)
                            break
                        else:
                            print("Invalid entry: input not between 0 and 9 (inclusive)")
                    except:
                        print("Invalid entry: please input a number between 0 and 9 (inclusive) or hit enter")

    def printBoard(self):
        for i in range(9):
            for j in range(9):
                value = self.getCell(i,j)
                if value == 0:
                    value = ' '
                if (j+1) % 3 == 0:
                    print(f"[{value}]", end=" ")
                else: 
                    print(f"[{value}]", end="")
            if (i+1) % 3 == 0:
                print("\n")
            else:
                print("")

    def getCell(self, row, col):
        return self.board[row][col]

    def setCell(self, row, col, val):
        self.board[row][col] = val

    def getRow(self, row):
        return self.board[row];

    def getCol(self, col):
        result = []
        for i in range(9):
            result.append(self.getCell(i, col))
        return result

    def getBox(self, row, col):
        r = (row // 3) * 3
        c = (col // 3) * 3
        result = []
        for i in range(3):
            for j in range(3):
                result.append(self.getCell(r+i, c+j))
        return result

    def solveCell(self, row, col):
        if self.getCell(row, col) != 0:
            return False

        nums = set(self.getRow(row) + self.getCol(col) + self.getBox(row, col))
        solutions = []

        for i in range(1, 10):
            if i not in nums:
                solutions.append(i)

        if len(solutions) == 1:
            self.setCell(row, col, solutions[0])
            return True

        return False
    

    def isSolved(self):
        for i in range(9):
            row = self.getRow(i)
            col = self.getCol(i)
            if not check_list(row) or not check_list(col):
                return False
        for i in range(3):
            box = self.getBox(i*3, i*3)
            if not check_list(box):
                return False
        return True


def check_list(list):
    if len(list) != 9:
        return False
    for i in range(1,10):
        if i not in list:
            return False
    return True


def main():
    # Get the sudoku problem and verify
    board = SudokuBoard()
    board.getState()
    board.printBoard()

    # While the problem is not solved, solve it
    solved = board.isSolved()
    while not solved:
        count = 0;
        for i in range(9):
            for j in range(9):
                if board.solveCell(i, j):
                    count += 1
        solved = board.isSolved()

    # Print the solved board
    board.printBoard()

main()
