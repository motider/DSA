class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        x = []
        for nums in image:
            nums.reverse()
            nums = [0 if x == 1 else 1 for x in nums]
            x.append(nums)

        return x
        