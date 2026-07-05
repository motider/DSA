class Solution(object):
    def majorityElement(self, nums):
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
                
        for key in freq:
            if freq[key] == max(freq.values()):
                return key

        """
        :type nums: List[int]
        :rtype: int
        """
        