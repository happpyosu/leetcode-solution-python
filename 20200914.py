from typing import List


# leetcode 1039 多边形三角剖分的最低得分
# dp[i][j] = min(dp[i][m] + A[m] * A[i] * A[j] + dp[m][j]) for m in range [i+1, j)
def minScoreTriangulation(self, A: List[int]) -> int:
    length = len(A)
    dp = [[float('inf')] * length for _ in range(length)]

    for i in range(length-1):
        dp[i][i+1] = 0

    for i in range(length - 3, -1, -1):
        for j in range(i+2, length, 1):
            for m in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][m] + A[m] * A[i] * A[j] + dp[m][j])

    return int(dp[0][length-1])




if __name__ == '__main__':
    A = [1, 3, 1, 4, 1, 5]
    min_val = minScoreTriangulation(0, A)
    print(min_val)
