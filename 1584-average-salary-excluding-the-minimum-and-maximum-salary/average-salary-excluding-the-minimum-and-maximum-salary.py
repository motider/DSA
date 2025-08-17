class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary.reverse()
        salary.pop()
        x = sum(salary)
        y = len(salary)
        z = x/y
        return z
        