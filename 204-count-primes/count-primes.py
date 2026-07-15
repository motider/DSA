class Solution(object):
    def countPrimes(self, n):
        if n == 0 or n == 1:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                is_prime[i*i : n : i] = [False] * len(range(i*i, n, i))
                
        primes = [i for i, prime in enumerate(is_prime) if prime]

        return len(primes)

        """
        :type n: int
        :rtype: int
        """
        