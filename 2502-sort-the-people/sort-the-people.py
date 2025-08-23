class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        y = []
        for i in zip(heights, names):
            y.append(i)    
        print(y)
        sorted_arr = sorted(y, reverse=True)
        final = []
        for h, name in sorted_arr:  
            final.append(name)
        return final



        