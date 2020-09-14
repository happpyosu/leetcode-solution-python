# leetcode 906. 超级回文数
# 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
# 思路：假设 P = R ** 2 是超级回文数，同时我们知道P的取值范围为[1, 1e18]，由此可知
# R的取值范围为[1, 1e9]，由于R也是一个回文数，不妨记为 k || k', 其中k是正常的数字
# 由此可知k大的可能取值范围为1e5, 有可能有以下情况1234321,或者是偶数个数位12344321
def superpalindromesInRange(L: str, R: str) -> int:
    magic = 100000
    L = int(L)
    R = int(R)
    def reverse(x):
        ans = 0
        while x != 0:
            ans = ans * 10 + x % 10
            x //= 10
        return ans

    def is_palindromes(x):
        return x == reverse(x)

    ans = 0
    # 处理 1234321
    for k in range(1, magic+1):
        s = str(k)
        t = s + s[-2::-1]
        v = int(t) ** 2
        if v > R:
            break
        if v >= L and is_palindromes(v):
            ans += 1

    for k in range(1, magic+1):
        s = str(k)
        t = s + s[::-1]
        v = int(t) ** 2
        if v > R:
            break
        if v >= L and is_palindromes(v):
            ans += 1

    return ans




if __name__ == '__main__':
    print(superpalindromesInRange('4', '1000'))
