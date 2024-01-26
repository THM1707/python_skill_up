from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        diff = 0

        for i in nums:
            if i < 10:
                continue

            diff += i - self.sum_of_digits(i)

        return diff

    def sum_of_digits(self, n: int):
        if n < 10:
            return n

        return n % 10 + self.sum_of_digits(int(n / 10))


def main():
    s = Solution()
    print(s.differenceOfSum([1, 15, 6, 3]))


if __name__ == '__main__':
    main()
