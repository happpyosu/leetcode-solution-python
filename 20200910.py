from typing import List


def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    dp = [[False] * n for _ in range(n)]
    for p, c in prerequisites:
        dp[p][c] = True

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] and dp[k][j]:
                    dp[i][j] = True
    ans = []
    for i, j in queries:
        ans.append(dp[i][j])
    return ans

