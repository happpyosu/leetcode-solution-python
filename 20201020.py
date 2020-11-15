from typing import List


# leetcode 930 和相同的二元子数组
# medium
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        preSum = 0
        m = {0: 1}
        ans = 0
        for e in A:
            preSum += e
            ans += m.get(preSum - S, 0)
            m[preSum] = m.get(preSum, 0) + 1
        return ans


# leetcode 1626. 无矛盾的最佳球队
# medium
# 思路: 按照年龄将对应的score进行排序分组, 然后在按照年龄先后组中选中一个最大的分数x, 那么以后在其他年龄组中就只能选择比x更大的球员了,
# 则可以按照年龄组的最大分数依次遍历。
class Solution2:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        a = sorted(zip(ages, scores))
        n = len(a)
        dp = [a[i][1] for i in range(n)]
        for i in range(n):
            cur_age, cur_score = a[i]
            for j in range(i):
                age, score = a[j]
                if cur_age == age or cur_score >= score:
                    dp[i] = max(dp[i], dp[j] + cur_score)

        return max(dp)

    def select(self, scores, y):
        a = len(scores)
        left = 0
        right = a - 1
        while left <= right:
            mid = (left + right) // 2
            if scores[mid] >= y:
                if mid == 0 or (scores[mid - 1] < y):
                    return mid

            if scores[mid] < y:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == '__main__':
    s = Solution2()


