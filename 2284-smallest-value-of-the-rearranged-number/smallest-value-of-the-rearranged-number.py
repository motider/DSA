class Solution(object):
    def smallestNumber(self, num):
        x = list(str(num))

        if num > 0:
            x.sort()
            if '0' in x:
                min_positive = min(n for n in x if int(n) > 0)
                idx = x.index(min_positive) 
                x[0], x[idx] = x[idx], x[0]
        elif num < 0:
            x.remove('-') 
            x.sort(reverse=True)
            x.insert(0, "-")

        return int("".join(x))
        """
        :type num: int
        :rtype: int
        """
        