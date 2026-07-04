class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        new = []
        for l in range(len(nums)-1):
            n = l+1
            r = len(nums)-1
            while n < r:
                x = nums[l]+nums[n]+nums[r]
                if x == 0:
                    new.append([nums[l], nums[n], nums[r]])
                    r-=1
                elif x < 0:
                    n+=1
                else:
                    r-=1
                    
        final = []
        for i in new:
            if i not in final:
                final.append(i)
        return final
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        