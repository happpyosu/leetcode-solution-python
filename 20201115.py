
# leetcode 1541. 平衡括号字符串的最少插入次数
# medium
class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)

        index = 0
        inc = 0
        left = 0

        while index < length:
            if s[index] == '(':
                left += 1
                index += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    inc += 1

                if index + 1 < length and s[index + 1] == ')':
                    index += 2
                else:
                    inc += 1
                    index += 1

        inc += left * 2
        return inc







