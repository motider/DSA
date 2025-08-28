class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        srs = 0
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] + nums[right] < target:
                    srs += 1
        return srs
 


                