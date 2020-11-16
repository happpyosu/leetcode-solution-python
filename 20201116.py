
# leetcode 1318. 或运算的最小翻转次数
# medium
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        inc = 0

        sa = bin(a)[2:]
        sb = bin(b)[2:]
        sc = bin(c)[2:]
        maxLen = max(len(sc), len(sa), len(sb))

        sa = '0'*(maxLen - len(sa)) + sa
        sb = '0'*(maxLen - len(sb)) + sb
        sc = '0'*(maxLen - len(sc)) + sc

        for (x, y, z) in zip(sa, sb, sc):
            if x == '0' and y == '1' and z == '0':
                inc += 1
            elif x == '1' and y == '0' and z == '0':
                inc += 1
            elif x == '1' and y == '1' and z == '0':
                inc += 2
            elif x == '0' and y == '0' and z == '1':
                inc += 1

        return inc

# leetcode9 回文数
# easy
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

# leetcode10 正则表达式匹配
# hard
# todo
class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        p = ' ' + p
        len_s = len(s)
        len_p = len(p)
        dp = [[False for _ in range(len_p + 1)] for _ in range(len_s + 1)]

        dp[0][0] = True
        for i in range(2, len_p+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]

        for i in range(1, len_s+1):
            for j in range(1, len_p+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = False

        return dp[len_s][len_p]


if __name__ == '__main__':
    solu = Solution3()

    s = 'aab'
    p = 'c*a*b'

    print(solu.isMatch(s, p))
