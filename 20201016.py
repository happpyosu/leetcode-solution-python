from typing import List


# leetcode 1528
# easy
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        tmp = [''] * len(s)
        for i in range(len(s)):
            tmp[indices[i]] = s[i]
        return ''.join(tmp)


class Solution2:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0:
            return []

        x = (tomatoSlices / 2 - cheeseSlices)
        y = (2 * cheeseSlices - tomatoSlices / 2)

        if x >= 0 and y >= 0:
            return [int(x), int(y)]
        else:
            return []


# leetcode 1504 统计全1的子矩形
# middle
class Solution3:
    # 采用单调栈优化的解法
    def numSubmatOpt(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        left = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(rows):
            for j in range(cols):
                if j == 0:
                    left[i][j] = mat[i][j]
                else:
                    left[i][j] = left[i][j - 1] + 1 if mat[i][j] == 1 else 0
        ans = 0
        for j in range(0, cols):
            stack = []  # stack中存放的是(left长度值， 被push进去的元素大于栈顶元素的个数)
            to_sum = 0
            for i in range(0, rows):
                cnt = 0
                while stack and stack[-1][0] > left[i][j]:
                    to_sum -= (stack[-1][1] + 1) * (stack[-1][0] - left[i][j])
                    cnt += stack[-1][1] + 1
                    stack.pop()
                to_sum += left[i][j]
                ans += to_sum
                stack.append((left[i][j], cnt))
        return ans

    # 采用左边数组的解法, 时间复杂度为O(n * n * m)
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        left = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(rows):
            for j in range(cols):
                if j == 0:
                    left[i][j] = mat[i][j]
                else:
                    left[i][j] = left[i][j - 1] + 1 if mat[i][j] == 1 else 0
        ans = 0
        for i in range(rows - 1, -1, -1):
            for j in range(0, cols):
                min_left = float('inf')
                for k in range(i, -1, -1):
                    min_left = min(min_left, left[k][j])
                    if min_left == 0:
                        break
                    ans += min_left

        return ans


if __name__ == '__main__':
    s = Solution3()
    mat = [[1, 1, 1, 1, 1, 1]]
    ans = s.numSubmat(mat)
    print(ans)
