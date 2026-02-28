class Solution(object):
    def findLucky(self, arr):
        x = []
        for i in arr:
            if arr.count(i) == i:
                x.append(i)
            else:
                x.append(-1)
        return max(x)
        """
        :type arr: List[int]
        :rtype: int
        """
        