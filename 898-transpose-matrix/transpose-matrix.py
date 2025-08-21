class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        count = []                         
        for i in zip(*matrix):             
            count.append(list(i))          

                            
        return count
        