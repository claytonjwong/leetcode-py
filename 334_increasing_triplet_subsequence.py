#
# 334. Increasing Triplet Subsequence
#
# Q: https://leetcode.com/problems/increasing-triplet-subsequence/
# A: https://leetcode.com/problems/increasing-triplet-subsequence/discuss/977048/Kt-Js-Py3-Cpp-Track-Two-Minimums
#

from typing import List

class Solution:
    def increasingTriplet(self, A: List[int], a = float('inf'), b = float('inf')) -> bool:
        for x in A:
            if x <= a:
                a = x
            elif x <= b:
                b = x
            else:
                return True
        return False
