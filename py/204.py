## reference: leetcode hint
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0

        isPrime = []
        for i in range(n):
            isPrime.append(True)
        isPrime[0] = isPrime[1] = False

        i = 2
        while i ** 2 < n:
            if isPrime[i] == False:
                pass
            else:
                for j in range(i ** 2, n, i):
                    isPrime[j] = False
            i += 1

        primeCount = 0
        for ip in isPrime:
            primeCount += 1 if ip else 0

        return primeCount


s = Solution()
print(s.countPrimes(4))