class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        z = y[::-1]

        for i in range(len(y)):
            if y[i] != z[i]:
                return False
                break
        else:
            return True

        """
        :type x: int
        :rtype: bool
        """
        