from typing import List

maxLen = 0


# leetcode1239 串联字符串的最大长度
# medium
class Solution:
    def dfs(self, arr, s, i):
        global maxLen
        maxLen = max(maxLen, len(s))
        for x in range(i, len(arr)):
            set1 = set(arr[x])
            if len(set1) != len(arr[x]):
                continue
            set2 = set(s)
            if len(set1 & set2) == 0:
                s2 = s + arr[x]
                self.dfs(arr, s2, x + 1)

    def maxLength(self, arr: List[str]) -> int:
        global maxLen
        maxLen = 0
        self.dfs(arr, '', 0)
        return maxLen


# leetcode 1345 跳跃游戏IV
# hard
class Solution2:
    def minJumps(self, arr: List[int]) -> int:
        m = {}
        dp = [-1] * len(arr)
        for i, e in enumerate(arr):
            if m.get(e, None) is None:
                m[e] = list()
            m[e].append(i)
        dp[0] = 0
        q = [0]

        while len(q) > 0:
            cur = q.pop()
            pos_list = m.get(arr[cur], [])
            for e in pos_list:
                if dp[e] == -1:
                    dp[e] = dp[cur] + 1
                    q.insert(0, e)

            pos_list.clear()
            if cur - 1 >= 0 and dp[cur - 1] == -1:
                dp[cur - 1] = dp[cur] + 1
                q.insert(0, cur - 1)

            if cur + 1 < len(arr) and dp[cur + 1] == -1:
                dp[cur + 1] = dp[cur] + 1
                q.insert(0, cur + 1)

            if dp[len(arr) - 1] != -1:
                return dp[len(arr) - 1]

        return dp[len(arr) - 1]


if __name__ == '__main__':
    arr = [7,6,9,6,9,6,9,7]
    s = Solution2()
    print(s.minJumps(arr))
