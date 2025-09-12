class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mountain = True
        if len(arr) < 3:
            mountain = False
        else:
            for i in range(len(arr) - 1):
                if arr[i] == arr[i + 1]:
                    mountain = False
                    break
            if mountain:
                maxim = max(arr)
                x = arr.index(maxim)
                if x == 0 or x == len(arr) - 1:
                    mountain = False
                else:
                    z = arr[:x]
                    for i in range(len(z) - 1):
                        if z[i] >= z[i + 1]:
                            mountain = False
                            break
                    if mountain:
                        array = arr[x:]
                        for j in range(len(array) - 1):
                            if array[j] <= array[j + 1]:
                                mountain = False
                                break
        return mountain

