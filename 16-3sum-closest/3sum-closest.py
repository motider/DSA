class Solution(object):
    def threeSumClosest(self, nums, target):
            nums.sort()
            closest = sum(nums[:3])
            n = len(nums)
            
            for i in range(n - 2):
                left, right = i + 1, n - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if abs(target - total) < abs(target - closest):
                        closest = total
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        return total  
            return closest

            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            