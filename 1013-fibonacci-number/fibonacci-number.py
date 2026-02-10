class Solution(object):
    def fib(self, n):
        x = [0,1]
        if n == 0:
            return 0
        for i in range(2,n):
            y = x[-1]+x[-2]
            x.append(y)
        return x[-1]+x[-2]
        """
        :type n: int
        :rtype: int
        """
        