from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def facto(n, to):
            ans = 1
            for i in range(n, to, -1):
                ans *= i
            return ans
        m-=1
        n-=1
        if m > n:
            return int(facto(m+n, m) / factorial(n))
        else:
            return int(facto(m+n, n) / factorial(m))