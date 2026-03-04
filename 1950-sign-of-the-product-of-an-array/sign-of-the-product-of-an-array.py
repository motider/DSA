class Solution(object):
    def arraySign(self, nums):
        from functools import reduce
        product_of_nums = reduce(lambda x,y : x*y,nums)

        if product_of_nums == 0:
            return 0
        elif product_of_nums < 0:
            return -1
        else:
            return 1
        """
        :type nums: List[int]
        :rtype: int
        """
        