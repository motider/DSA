class Solution(object):
    def tribonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        x = [0,1,1]
        for i in range(3,n):
            y = x[-3]+x[-2]+x[-1]
            x.append(y)
        return x[-3]+x[-2]+x[-1]
        """
        :type n: int
        :rtype: int
        """
        