class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
            x = []
            sorted_array = []
            count = 0   
            for i in zip(*strs):     
                y = "".join(i)       
                x.append(y)
                arr = sorted(y)      
                joined = "".join(arr)
                sorted_array.append(joined)
            for j in range(len(x)):  
                if x[j] != sorted_array[j]:
                    count += 1

            return count