from collections import defaultdict
from typing import List, Dict


# leetcode
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


# leetcode 1203 项目管理
# hard


class Solution2:

    def topoSort(self, grid):
        count = {u: 0 for u in grid}  # 记录依赖数
        for u in grid:
            for v in grid[u]:
                count[v] += 1
        queue = [u for u in grid if count[u] == 0]
        ans = []
        while queue:
            u = queue.pop()
            ans.append(u)

            for v in grid[u]:
                count[v] -= 1
                if count[v] == 0:
                    queue.append(v)
        return ans

    def sortItems(self, n, m, group, beforeItems):
        item_grids = {}
        group_grid = defaultdict(set)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

            if group[i] not in item_grids:
                item_grids[group[i]] = defaultdict(list)

            if i not in item_grids[group[i]]:
                item_grids[group[i]][i] = []

            if group[i] not in group_grid:
                group_grid[group[i]] = set()

        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    item_grids[group[i]][j].append(i)  # item_grids[i][j]表示第i组中item为j的项目依赖的组, 即组内依赖
                else:
                    group_grid[group[j]].add(group[i])  # 如果依赖属于不同组, 则放入group_grid中处理, 表示依赖的set
        print(item_grids)
        print(group_grid)

        ans = []
        groups_order = self.topoSort(group_grid)
        for i in groups_order:
            item_grid = item_grids.get(i)
            if not item_grid:
                continue

            items_order = self.topoSort(item_grid)
            if len(items_order) != len(item_grid):
                return []
            ans.extend(items_order)

        return ans if len(ans) == n else []


class Review2:

    # def topoSort(self, grid: dict[int, set]):
    #     queue = []
    #     order = []
    #     for k in grid:
    #         if len(grid[k]) == 0:
    #             queue.insert(0, k)
    #     while queue:
    #         cur = queue.pop()
    #         order.append(cur)
    #         for k in grid:
    #             grid[k].discard(cur)


    def sortItems(self, n, m, group, beforeItems):
        item_grid = {}
        group_grid = {}

        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        for i in range(n):
            g = group[i]
            dep = beforeItems[i]

            if g not in item_grid:
                item_grid[g] = defaultdict(list)

            if g not in group_grid:
                group_grid[g] = set()

            if len(dep) == 0:
                item_grid[g][i] = []
            else:
                for d in dep:
                    if group[d] == g:
                        item_grid[g][i].append(d)
                    else:
                        group_grid[g].add(group[d])
        print(group_grid)
        print(item_grid)


def climb(n: int, k: int):
    dp1 = [0] * (n+1)
    dp2 = [0] * (n+1)
    dp1[0] = 1
    dp1[1] = 1
    dp1[2] = 2
    for i in range(3, n+1):
        dp1[i] = dp1[i-1] + dp1[i-2] + dp2[i-1] + dp2[i-2]
        dp2[i] += dp1[i-3]
        cur = i
        temp = k
        flag = True
        while cur >= 0 and temp > 0:
            cur -= 3
            temp -= 1
            if dp2[cur] != 0:
                flag = False
            if flag:
                dp2[i] += dp2[i-3]

    return dp1[n] + dp2[n]


if __name__ == '__main__':
    print(climb(6, 1))










