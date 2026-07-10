class Solution(object):
    def kthLargestNumber(self, nums, k):
        new = [int(i) for i in nums]
        new.sort()
        return str(new[-k])
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        