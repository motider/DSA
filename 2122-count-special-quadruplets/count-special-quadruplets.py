class Solution(object):
    def countQuadruplets(self, nums):
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            count+=1
        return count
                    
        """
        :type nums: List[int]
        :rtype: int
        """
        