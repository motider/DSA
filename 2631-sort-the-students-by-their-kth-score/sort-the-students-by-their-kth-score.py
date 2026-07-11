class Solution(object):
    def sortTheStudents(self, score, k):
        new = sorted(score,key = lambda x: x[k],reverse = True)
        return new
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        