class Solution(object):
    def findRestaurant(self, list1, list2):
        maps = {}

        for i in list1:
            if i in list2:
                maps[i] = list1.index(i) + list2.index(i)
                
        new = list(maps.items())

        fin = [i[1] for i in new]
        ans = []
        for j in new:
            if j[1] == min(fin):
                ans.append(j[0])
                
        return ans
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        