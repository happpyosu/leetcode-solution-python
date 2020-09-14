
# leetcode 1371 每个元音包含偶数次的最长子字符串
def findTheLongestSubstring(self, s: str) -> int:
    dp = [-float('inf')] * 32
    dp[0] = -1
    pattern = 0
    max_len = 0
    for i in range(len(s)):
        if s[i] == 'a':
            pattern ^= 1
        elif s[i] == 'e':
            pattern ^= 2
        elif s[i] == 'i':
            pattern ^= 4
        elif s[i] == 'o':
            pattern ^= 8
        elif s[i] == 'u':
            pattern ^= 16

        if dp[pattern] != -float('inf'):
            max_len = max(max_len, i - dp[pattern])
        else:
            dp[pattern] = i

    return max_len



if __name__ == '__main__':

    substring = findTheLongestSubstring(0, 'eleetminicoworoep')
    print(substring)