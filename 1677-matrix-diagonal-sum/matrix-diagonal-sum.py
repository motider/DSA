class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
    
        count = []
        for i in range(len(mat)):       
            for j in range(len(mat[i])):  
                if i == j:               
                    count.append(mat[i][j])
        fex = []
        for element in mat:
            z = element[::-1]
            fex.append(z)
        fin = []
        for yes in range(len(fex)):
            for no in range(len(fex[yes])):
                if yes == no:
                    fin.append(fex[yes][no])
        com = fin + count
        if len(mat) % 2 == 1:
            mid = len(mat) // 2
            com.remove(mat[mid][mid])

        return sum(com)


