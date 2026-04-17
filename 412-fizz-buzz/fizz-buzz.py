class Solution(object):
    def fizzBuzz(self, n):
        new = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                new.append("FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                new.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                new.append("Buzz")
            else:
                new.append(str(i))
        return new
        """
        :type n: int
        :rtype: List[str]
        """
        