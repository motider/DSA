class Solution(object):
    def frequencySort(self, nums):
        y = list(map(lambda x:nums.count(x),nums))

        zipped_list = list(zip(nums,y))

        new_arr = sorted(zipped_list, key = lambda x : (x[1],-x[0]) )
        final = []
        for i in new_arr:
            final.append(i[0])
        return final       
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        