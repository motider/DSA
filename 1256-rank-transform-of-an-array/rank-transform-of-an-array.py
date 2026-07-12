class Solution(object):
    def arrayRankTransform(self, arr):
        unique_sorted = sorted(list(set(arr)))
        rank_map = {}
        for index, num in enumerate(unique_sorted):
            rank_map[num] = index + 1

        ans = []
        for num in arr:
            ans.append(rank_map[num])

        return ans 
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        