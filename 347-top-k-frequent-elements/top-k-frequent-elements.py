class Solution(object):
    def topKFrequent(self, nums, k):
        x = {}
        for num in nums:
            if num in x:
                x[num] += 1
            else:
                x[num] = 1
                
        items = list(x.items())
        items.sort(key=lambda x: x[1], reverse=True)

        new = []
        for i in range(k):
            new.append(items[i][0])

        return new

        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        