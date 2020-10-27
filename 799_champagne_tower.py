#
# 799. Champagne Tower
#
# Q: https://leetcode.com/problems/champagne-tower/
# A: https://leetcode.com/problems/champagne-tower/discuss/118694/Kt-Js-Py3-Cpp-The-ART-of-Dynamic-Programming
#

# bottom-up
class Solution:
    def champagneTower(self, K: int, M: int, N: int) -> float:
        dp = [[0] * (N + 2) for _ in range(M + 1)]
        dp[0][0] = K
        for i in range(M):
            for j in range(N + 1):
                if dp[i][j] <= 1.0:  # no overflow
                    continue
                half = (dp[i][j] - 1.0) / 2  # -1.0 to fill cup i,j
                dp[i + 1][j]     += half
                dp[i + 1][j + 1] += half
        return min(dp[M][N], 1.0)

# memory optimized
class Solution:
    def champagneTower(self, K: int, M: int, N: int) -> float:
        pre = [0.0] * (N + 2)
        pre[0] = K
        for _ in range(M):
            cur = [0.0] * (N + 2)
            for j in range(N + 1):
                if pre[j] <= 1.0:  # no overflow
                    continue
                half = (pre[j] - 1.0) / 2  # -1.0 to fill cup i,j
                cur[j]     += half
                cur[j + 1] += half
            pre, cur = cur, pre
        return min(pre[N], 1.0)
