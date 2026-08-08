class Solution(object):
    def transpose(self, matrix):
        new = []

        for i in zip(*matrix):
            new.append(list(i))

        return new

        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        