#
# 1041. Robot Bounded In Circle
#
# Q: https://leetcode.com/problems/robot-bounded-in-circle/
# A: https://leetcode.com/problems/robot-bounded-in-circle/discuss/294269/Javascript-Python3-C%2B%2B-Traverse-4x-%2B-Return-to-Origin
#

class Solution:
    def isRobotBounded(self, A: str, K = 4) -> bool:
        U, R, D, L = [i for i in range(4)]                       # 🗺 clockwise directions
        x, y = 0, 0                                              # ⭐️ origin
        dir = U
        while K:                                                 # 🔍 can we return to ⭐️ origin within 4 traversals?
            for c in A:
                if c == 'G':                                     # 🚌 step forward
                    if dir == U: x -= 1
                    if dir == D: x += 1
                    if dir == L: y -= 1
                    if dir == R: y += 1
                if c == 'L': dir = L if dir == U else dir - 1    # 👈 turn left
                if c == 'R': dir = U if dir == L else dir + 1    # 👉 turn right
                print(x, y)
            if not x and not y:
                return True                                      # 🎯 returned to ⭐️ origin after 1, 2, or 4 traversals
            K -= 1
        return False
