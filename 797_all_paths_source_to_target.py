#
# 797. All Paths From Source to Target
#
# Q: https://leetcode.com/problems/all-paths-from-source-to-target/
# A: https://leetcode.com/problems/all-paths-from-source-to-target/discuss/752917/Javascript-Python3-C%2B%2B-DFS-%2B-BT
#

class Solution:
    def allPathsSourceTarget(self, adj: List[List[int]]) -> List[List[int]]:
        paths = []
        N = len(adj)
        s, t = 0, N - 1
        def go(u = s, path = [ s ]):
            if u == t:
                paths.append(path[:]) # 🎯 target t reached
            else:
                for v in adj[u]:
                    go(v, path + [v]) # 🚀 explore edge u -> v with implicit ✅ 👀 forward-tracking + 🚫 👀 back-tracking
        go()
        return paths
