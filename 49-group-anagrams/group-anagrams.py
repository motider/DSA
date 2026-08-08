class Solution(object):
    def groupAnagrams(self, strs):
        freq = defaultdict(list)

        for i in range(len(strs)):
            y = "".join(sorted(strs[i]))
            freq[y].append(strs[i])

        ans = []
        for i in freq:
            ans.append(freq[i])

        return ans

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        