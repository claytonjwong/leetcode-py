#
# 1567. Maximum Length of Subarray With Positive Product
#
# Q: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
# A: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/discuss/822464/Javascript-Python3-C%2B%2B-Sliding-Window
#

class Solution:
    def getMaxLen(self, A: List[int], cnt = 0, best = 0) -> int:
        A.append(0)  # ⭐️ sentinel value
        N = len(A)
        i = 0
        j = 0
        while i != N:
            # case 1: ➖ collapse window [i 👉 ..j]
            while j < N and not A[j]:
                while i < j:
                    cnt = cnt - 1 if A[i] < 0 else cnt; i += 1
                    best = best if cnt & 1 else max(best, j - i)
                i = j + 1
                j = j + 1
            # case 2: ➕ expand window [i..j 👉 ]
            while j < N and A[j]:
                cnt = cnt + 1 if A[j] < 0 else cnt; j += 1
                best = best if cnt & 1 else max(best, j - i)
        return best
