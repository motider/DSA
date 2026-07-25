class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        n = len(arr) * 0.05

        new = arr[int(n):int((len(arr)-n))]

        x = 0
        for i in new:
            x+=i
            
        return x/float(len(new))
        """
        :type arr: List[int]
        :rtype: float
        """
        