class Solution(object):
    def multiply(self, num1, num2):
        digit_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        result = 0
        sign = 1

        if num1[0] == '-':
            sign = -1
            num1 = num1[1:]
        elif num1[0] == '+':
            num1 = num1[1:]

        for char in num1:
            digit_value = digit_map[char]
            result = result * 10 + digit_value

        final_output = sign * result

        result2 = 0
        sign2 = 1
        if num2[0] == '-':
            sign = -1
            num2 = num2[1:]
        elif num2[0] == '+':
            num2 = num2[1:]

        for char in num2:
            digit_value2 = digit_map[char]
            result2 = result2 * 10 + digit_value2

        final_output2 = sign2 * result2
        return str(final_output2 * final_output)
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        