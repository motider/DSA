class Solution(object):
    def countEven(self, num):
        coun = []
        for i in range(num + 1) :
            y = str(i)
            x = list(y)
            new = []
            for j in x:
                new.append(int(j))
            coun.append(sum(new))
        final = 0
        for n in coun:
            if n % 2 == 0 and n != 0:
                final += 1
        return final
        """
        :type num: int
        :rtype: int
        """
        