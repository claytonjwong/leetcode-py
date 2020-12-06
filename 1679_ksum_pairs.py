#
# 1679. Max Number of K-Sum Pairs
#
# Q: https://leetcode.com/problems/max-number-of-k-sum-pairs/
# A: https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/962118/Kt-Js-Py3-Cpp-Map
#

from typing import List

class Solution:
    def maxOperations(self, A: List[int], k: int, pairs = 0) -> int:
        m = {}
        for x in A:
            y = k - x
            if y not in m:
                m[x] = 1 + m[x] if x in m else 1
                continue
            pairs += 1
            m[y] -= 1
            if not m[y]:
                del m[y]
        return pairs
