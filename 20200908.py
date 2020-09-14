from typing import List


# leetcode 1577 数的平方等于两数乘积的方法数

def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
    map1 = {}
    map2 = {}
    c = 0

    for i in range(len(nums1)):
        v = nums1[i]
        li = map1.get(v, [])
        li.append(i)
        map1[v] = li

    for i in range(len(nums2)):
        v = nums2[i]
        li = map2.get(v, [])
        li.append(i)
        map2[v] = li

    for x in nums1:
        s = x ** 2
        for i in range(len(nums2)):
            v = nums2[i]
            if s % v == 0:
                l = map2.get(int(s / v), [])
                for e in l:
                    if e > i:
                        c += 1

    for x in nums2:
        s = x ** 2
        for i in range(len(nums1)):
            v = nums1[i]
            if s % v == 0:
                l = map1.get(int(s / v), [])
                for e in l:
                    if e > i:
                        c += 1
    return c


if __name__ == '__main__':
    nums1 = [7, 7, 8, 3]
    nums2 = [1, 2, 9, 7]
    c = numTriplets(self=0, nums1=nums1, nums2=nums2)
    print(c)
