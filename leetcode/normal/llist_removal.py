from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next_node: Optional['ListNode'] = None):
        self.val = val
        self.next_node = next_node


class Solution:
    @staticmethod
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        node = head

        while node is not None:
            node = node.next_node
            l += 1

        if n >= l:
            return head

        left_node = head
        for _ in range(l - n):
            left_node = left_node.next_node

        if n == 1:
            left_node.next_node = None
            return head

        right_node = left_node.next_node.next_node
        left_node.next_node = right_node

        return head
