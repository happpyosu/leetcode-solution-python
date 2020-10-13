# leetcode 1553 吃掉N个橘子的最少天数
# def minDays(self, n: int) -> int:
#     if n == 1:
#         return 1
#     if n == 2 or n == 3:
#         return 2
#
#     dp = [0] * (n)
#     dp[0] = 1
#     dp[1] = 2
#     dp[2] = 2
#
#     for i in range(3, n):
#         c = i+1
#         a1 = 1 + dp[c-2]
#         a2 = float('inf')
#         a3 = float('inf')
#
#         if c % 2 == 0:
#             a2 = 1 + dp[c - c // 2 - 1]
#
#         if c % 3 == 0:
#             a3 = 1 + dp[c - 2 * (c // 3) - 1]
#
#         dp[i] = min(a1, a2, a3)
#
#     return dp[n-1]

map = {}

# leetcode 1553 吃掉N个橘子的最少天数
class Solution:
    def minDays(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2 or n == 3:
            return 2

        re = map.get(n, None)
        if re is not None:
            return re

        m2 = self.minDays(n=n//2) + n % 2
        m3 = self.minDays(n=n//3) + n % 3
        result = min(m2, m3) + 1
        map[n] = result

        return result

