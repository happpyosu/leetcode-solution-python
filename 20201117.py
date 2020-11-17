# leetcode 12 整数转罗马数字
# medium


class Solution:
    def intToRoman(self, num: int) -> str:
        m = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
             500: 'D', 900: 'CM', 1000: 'M'}
        a = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        def bin_search(x, start, end):
            if start > end:
                return -1
            l = start
            r = end
            while l <= r:
                mid = (l + r) // 2
                if a[mid] > x:
                    r = mid - 1
                elif a[mid] < x:
                    res = bin_search(x, start + 1, end)
                    if res < 0:
                        return mid
                    else:
                        return res
                else:
                    return mid

            return -1

        s = str()
        while num > 0:
            idx = bin_search(num, 0, len(m) - 1)
            s = s + m[a[idx]]
            num -= a[idx]

        return s


if __name__ == '__main__':
    s = Solution()
    roman = s.intToRoman(9)
    print(roman)
