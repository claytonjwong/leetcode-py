#
# 1519. Number of Nodes in the Sub-Tree With the Same Label
#
# Q: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
# A: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/discuss/746462/Javascript-Python3-C%2B%2B-post-order-traversal
#

class Solution:
    def countSubTrees(self, N: int, E: List[List[int]], keys: str) -> List[int]:
        ans = [0] * N
        seen = set()
        adj = list(map(lambda _: [], [None] * N))
        for [u, v] in E:
            adj[u].append(v)
            adj[v].append(u)
        def go(u = 0) -> List[int]:
            seen.add(u) # seen u 👀
            next = [0] * 26
            for v in adj[u]:
                if v in seen: # 🚫 skip previously seen parent 👀
                    continue
                cur = go(v) # 🚀 explore child v 
                for key in range(26):
                    next[key] += cur[key] # 🎯 post-order accumulate keys for child node v
            key = ord(keys[u]) - ord('a')
            next[key] += 1 # 🎯 post-order increment key for current node u
            ans[u] = next[key]
            return next
        go()
        return ans
