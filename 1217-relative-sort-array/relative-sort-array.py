class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        x = []
        y = []

        for i in arr1:
            if i in arr2:
                x.append(i)
            else:
                y.append(i)

        new = sorted(x, key=lambda x: arr2.index(x))
        y.sort()

        return new + y
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        