#
# 1602. Find Nearest Right Node in Binary Tree
#
# Q: https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/
# A: https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/discuss/875464/Javascript-Python3-C%2B%2B-BFS-solutions
#

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findNearestRightNode(self, root: TreeNode, T: TreeNode) -> TreeNode:
        q = deque([ root ])
        while len(q):
            next = deque()
            while len(q):
                node = q.popleft()
                if node == T:
                    return q[0] if len(q) else None
                if node.left:  next.append(node.left)
                if node.right: next.append(node.right)
            [q, next] = [next, q]
        return None
