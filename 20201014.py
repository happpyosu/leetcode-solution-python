import math


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_num = 0
        for i in range(1, n+1):
            if self.isPrime(i):
                prime_num += 1
        return (math.factorial(prime_num) * math.factorial(n - prime_num)) % (10 ** 9 + 7)

    def isPrime(self, n: int) -> bool:
        if n == 1:
            return False
        tmp = n ** 0.5
        for i in range(2, int(tmp) + 1):
            if n % i == 0:
                return False
        return True

# leetcode 857. 雇佣 K 名工人的最低成本
# hard
class Solution1:
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        import heapq
        workers = sorted((Fraction(w, q), q, w) for q, w in zip(quality, wage))
        ans = float('inf')

        pool = []
        quality_sum = 0

        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            quality_sum += q

            if len(pool) > K:
                quality_sum += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * quality_sum)

        return float(ans)


def is_prime(x):
    if x == 1:
        return False

    if x % 6 != 1 or x % 6 != 5:
        return False

    root = int(x ** 0.5)
    for i in range(5, root+1, 6):
        if x % i == 0 or x % (i+2) == 0:
            return False

    return True


if __name__ == '__main__':
    s = Solution1()
    s.mincostToHireWorkers()