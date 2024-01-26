# /make-array-zero-by-subtracting-equal-amounts/description/
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(i for i in nums if i)
        return len(s)


def main():
    s = Solution()
    print(s.minimumOperations([0]))


if __name__ == '__main__':
    main()
