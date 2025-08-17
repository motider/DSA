class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            x= int( num / 3)
            y = x-1,x,x+1
            return list(y)
        else:
            return list()
           