class Solution(object):
    def findDiagonalOrder(self, mat):
        diagonal = defaultdict(list)
        row = len(mat)
        col = len(mat[0])
        for r in range(row):
            for c in range(col):
                key = r + c
                diagonal[key].append(mat[r][c])

        res = []
        for key,value in diagonal.items():
            if key % 2 == 0:
                res.extend(value[::-1])
            else:
                res.extend(value)

        return res
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        