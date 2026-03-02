class Solution(object):
    def kthDistinct(self, arr, k):
        y = [i for i in arr if arr.count(i) == 1]

        if len(y) < k:
            x = ""
            return x
        elif len(y) >= k:
            return y[k-1]
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        