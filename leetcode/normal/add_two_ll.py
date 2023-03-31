from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            return l1 or l2

        cur: Optional[ListNode]
        prev: Optional[ListNode]

        head1 = l1
        head2 = l2
        len1 = len2 = 0
        tmp = 0

        while l1 or l2:
            if l1 is None:
                l1 = ListNode(0, None)
            else:
                len1 += 1
            if l2 is None:
                l2 = ListNode(0, None)
            else:
                len2 += 1

            s = l1.val + l2.val + tmp
            if s >= 10:
                l1.val = l2.val = s % 10
                tmp = 1
            else:
                l1.val = l2.val = s
                tmp = 0
            l1 = l1.next
            l2 = l2.next

        if tmp == 1:
            l2.next = ListNode(1, None)

        if len1 < len2:
            return head2

        return head1
