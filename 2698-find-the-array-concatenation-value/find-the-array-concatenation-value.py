class Solution(object):
    def findTheArrayConcVal(self, nums):
        l = 0
        r = len(nums)-1
        total_sum = 0
        while l < r:
                y = str(nums[l]) + str(nums[r])
                total_sum += int(y)
                l+=1
                r-=1
        if len(nums) % 2 != 0:
            total_sum += nums[len(nums)//2]
                
        return total_sum
        """
        :type nums: List[int]
        :rtype: int
        """
        