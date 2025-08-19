class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        x = len(matrix)
        y= len(matrix[0])

        for i in range(1, x):
            for j in range(1, y):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
                    break
        return True
        