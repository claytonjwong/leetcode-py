#
# 1504. Count Submatrices With All Ones
#
# Q: https://leetcode.com/problems/count-submatrices-with-all-ones/
# A: https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/762330/Javascript-Python3-C%2B%2B-brute-force
#

from typing import List

class Solution:
    def numSubmat(self, A: List[List[int]], ans = 0) -> int:
        def go(row, col, M, N, cnt = 0):
            i = row
            while i < M:
                j = col
                while j < N:
                    if A[i][j]:
                        cnt += 1
                    else:
                        N = j
                    j += 1
                i += 1
            return cnt
        M = len(A)
        N = len(A[0])
        for i in range(M):
            for j in range(N):
                ans += go(i, j, M, N) # 🎯 count of all submatrices starting with i,j as top-left corner
        return ans
