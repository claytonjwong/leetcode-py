#
# 1539. Kth Missing Positive Number
#
# Q: https://leetcode.com/problems/kth-missing-positive-number/
# A: https://leetcode.com/problems/kth-missing-positive-number/discuss/780016/Javascript-Python3-C%2B%2B-Seen-values
#

from typing import List

class Solution:
    def findKthPositive(self, A: List[int], K: int) -> int:
        seen = set(A)
        i = 1
        while True:
            if not i in seen:
                K -= 1
                if K == 0:
                    return i
            i += 1
