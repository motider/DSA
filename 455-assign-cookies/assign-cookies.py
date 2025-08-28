class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gif = sorted(g)
        sif = sorted(s)
        left = 0   
        right = 0  
        count = 0
        while left < len(gif) and  right < len(sif):
                if sif[right] >= gif[left]:  
                    count += 1
                    left += 1   
                    right += 1  
                else:
                    right += 1  
        return count


                