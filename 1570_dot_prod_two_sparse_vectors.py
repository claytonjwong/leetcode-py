#
# 1570. Dot Product of Two Sparse Vectors
#
# Q: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
# A: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/discuss/826785/Javascript-Python3-C%2B%2B-Zip-solutions
#

from typing import List

class SparseVector:
    def __init__(self, A: List[int]):
        self.A = A
    def dotProduct(self, other: 'SparseVector') -> int:
        return sum([a * b for a, b in zip(self.A, other.A)])
