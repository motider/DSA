class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        freq ={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            if i not in freq:
                freq[i]=1
                
        new = []
        for key in freq:
            if freq[key] > len(nums)/3:
                new.append(key)
        return new
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        