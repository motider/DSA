class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        freq = {}
        found = False

        for idx, i in enumerate(nums):
            if i in freq and (idx - freq[i]) <= k:
                return True
                found = True
                break
            freq[i] = idx

        if not found:
            return False
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        