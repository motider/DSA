class Solution(object):
    def countDigits(self, num):
        x = str(num)
        y = list(x)

        new = [int(i) for i in y]
        count = 0
        for i in new:
            if num % i == 0:
                count+=1
        return count
        """
        :type num: int
        :rtype: int
        """
        