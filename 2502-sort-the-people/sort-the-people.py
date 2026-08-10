class Solution(object):
    def sortPeople(self, names, heights):
        m = {}
        for i in range(len(heights)):
            if heights[i] in m:
                m[heights[i]].append(names[i])
            else:
                m[heights[i]] = [names[i]]
        ans = []
        for i in sorted(list(m.keys()),reverse = True):
            m[i].sort()
            ans.extend(m[i])
        return ans
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        