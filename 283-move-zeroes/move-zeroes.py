class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = left + 1
        while right < len(nums):
            if nums[left] == 0 and right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != 0:  
                left += 1
            if right < len(nums):  
                right += 1

        return  nums

