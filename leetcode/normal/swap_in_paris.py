from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=Optional['ListNode']):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        idx = 0
        result = head.next
        cur = head
        prev = None

        while cur is not None:
            if idx % 2 == 0:
                new_cur = self.do_swap(cur, prev)

            idx += 1

            if new_cur is None:
                break

            prev = new_cur
            cur = prev.next

        return result

    def do_swap(self, cur: Optional[ListNode], prev: Optional[ListNode]) -> bool:
        following = cur.next

        if following is None:
            return None

        cur.next = following.next
        following.next = cur

        if prev is not None:
            prev.next = following

        return following
