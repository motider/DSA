class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = len(digits)-1
        y = digits[x] + 1
        digits.pop()
        digits.insert(x, y)

        while digits[x] == 10:   
            digits[x] = 0
            x -= 1
            if x < 0:            
                digits.insert(0, 1)
                break
            digits[x] += 1

        return digits

        
        