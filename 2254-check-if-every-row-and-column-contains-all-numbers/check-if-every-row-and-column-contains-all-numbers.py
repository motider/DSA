class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)

        is_valid = True

        for row in matrix:
            if len(row) != len(set(row)):
                is_valid = False
                break
            for i in row:
                if i < 1 or i > n:
                    is_valid = False
                    break

        if is_valid:
            for col in zip(*matrix):
                if len(col) != len(set(col)):
                    is_valid = False
                    break
                for j in col:
                    if j < 1 or j > n:
                        is_valid = False
                        break

        if is_valid:
            return True
        else:
            return False

        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        