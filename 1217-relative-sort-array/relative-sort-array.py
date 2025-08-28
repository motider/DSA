class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x = []
        y = sorted(arr1)
        for num in arr2:
            x.extend([num] * arr1.count(num))
        for num in y:
            if num not in arr2:
                x.append(num)
        return x
