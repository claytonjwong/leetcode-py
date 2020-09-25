#
# 2. Add Two Numbers
#
# Q: https://leetcode.com/problems/add-two-numbers/
# A: https://leetcode.com/problems/add-two-numbers/discuss/1093/Javascript-Python3-C%2B%2B-Concise-solutions
#

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, a: ListNode, b: ListNode) -> ListNode:
        ans = ListNode()
        head = ans
        carry = 0
        while True:
            head.val = (a.val if a else 0) + (b.val if b else 0) + carry
            carry = head.val // 10
            head.val %= 10
            a = a.next if a else None
            b = b.next if b else None
            if not a and not b and not carry:
                break
            head.next = ListNode()
            head = head.next
        return ans
