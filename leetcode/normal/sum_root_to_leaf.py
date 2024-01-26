# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0

        def get_sum_val(node: TreeNode, val: int) -> int:
            nonlocal s

            if not (node.left and node.right):
                s += val
            if node.left:
                get_sum_val(node.left, val * 10)
            if node.right:
                get_sum_val(node.right, val * 10)

        get_sum_val(root, root.val)

        return s


def main():
    s = Solution()


if __name__ == '__main__':
    main()
