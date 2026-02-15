class Solution(object):
    def addDigits(self, num):
        x = str(num)
        while len(x) > 1:
            y = list(x)
            arr = [int(item) for item in y]
            x = str(sum(arr))  
            
        return int(x) 

        """
        :type num: int
        :rtype: int
        """
        