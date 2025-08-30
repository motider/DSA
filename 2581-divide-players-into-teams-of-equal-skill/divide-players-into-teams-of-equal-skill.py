class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        x = []
        while left < right:
            if skill[left] + skill[right] == skill[left+1] + skill[right-1]:
                x.append(skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1
                break
        else:   
            return sum(x)
        