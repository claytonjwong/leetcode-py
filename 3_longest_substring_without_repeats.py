#
# 3. Longest Substring Without Repeating Characters
#
# Q: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# A: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/504179/Javascript-Python3-C%2B%2B-Previously-Seen-Duplicate
#

class Solution:
    def lengthOfLongestSubstring(self, S: str, pre = -1, big = 0) -> int:
        m = {}
        for i, c in enumerate(S):
            pre = max(pre, m[c] if c in m else -1); m[c] = i  # 👀 track index of previously seen duplicate
            big = max(big, i - pre)                           # 🎯 maximum substring length without duplicate
        return big
