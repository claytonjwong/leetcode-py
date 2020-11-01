#
# 1640. Check Array Formation Through Concatenation
#
# Q: https://leetcode.com/problems/check-array-formation-through-concatenation/
# A: https://leetcode.com/problems/check-array-formation-through-concatenation/discuss/919391/Kt-Js-Py3-Cpp-Do-we-%22have%22-what-we-%22need%22
#

from typing import List
from collections import deque

class Solution:
    def canFormArray(self, need: List[int], have: List[List[int]]) -> bool:
        q = deque()
        for x in need:
            if q:
                if x != q[0]:
                    return False
                q.popleft()
                continue
            found = False
            for piece in have:
                if x == piece[0]:
                    found = True
                    q.extend(piece[1:])
                    break
            if not found:
                return False
        return True
