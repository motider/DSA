class Solution(object):
    def isValidSudoku(self, board):
        clean_board = []
        for row in board:
            clean_row = [char for char in row if char != "."]
            clean_board.append(clean_row)

        new = []
        for col in zip(*board):
            clean_col = [char for char in col if char != "."]
            new.append(clean_col)

        boxes = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[r][c] for r in range(i, i + 3) for c in range(j, j + 3) if board[r][c] != "."]
                boxes.append(box)

        is_valid = True

        for i in clean_board:
            if len(set(i)) != len(i):
                is_valid = False
                break

        if is_valid:
            for j in new:
                if len(set(j)) != len(j):
                    is_valid = False
                    break

        if is_valid:
            for b in boxes:
                if len(set(b)) != len(b):
                    is_valid = False
                    break

        if is_valid:
            return True
        else:
            return False



        """
        :type board: List[List[str]]
        :rtype: bool
        """
        