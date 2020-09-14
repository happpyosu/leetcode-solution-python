from typing import List


# 课程表2
# leetcode 210
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    queue = []
    res = []
    a = [[] for i in range(numCourses)]
    for x in prerequisites:
        a[x[0]].append(x[1])

    for i in range(len(a)):
        if len(a[i]) == 0:
            queue.append(i)

    while queue:
        b = queue.pop(0)
        res.append(b)
        for i, x in enumerate(a):
            if b in x:
                x.remove(b)
                if len(x) == 0:
                    queue.append(i)

    for x in a:
        if len(x) != 0:
            return []

    return res



if __name__ == '__main__':
    pass
