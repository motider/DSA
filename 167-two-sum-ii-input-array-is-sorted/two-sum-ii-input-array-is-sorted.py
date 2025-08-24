class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                x = left + 1 , right + 1 
                return list(x)  
                break
            elif s < target:
                left += 1   
            else:
                right -= 1
          