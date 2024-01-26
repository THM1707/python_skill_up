from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    value: Any
    next: Optional["Node"]


@dataclass
class Queue:
    head: Optional[Node]
    tail: Optional[Node]
    length: int

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, val: Any):
        node = Node(val, None)
        self.length += 1

        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> Optional[Node]:
        self.length -= 1

        if not self.head:
            return None

        head = self.head
        self.head = self.head.next
        head.next = None

        if self.length == 0:
            self.tail = None

        return head.value

    def peek(self) -> Any:
        if self.head:
            return self.head.value
        return None
