from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        target_index = 1
        last = -1

        if len(nums) <= 1:
            return

        while 1:
            if nums[-target_index - 1] < nums[-target_index]:
                break
            target_index += 1

        left = len(nums) - target_index
        right = len(nums) - 1

        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1

        for i in range(len(nums) - target_index, len(nums)):
            if nums[i] > nums[len(nums) - target_index - 1]:
                tmp = nums[i]
                nums[i] = nums[len(nums) - target_index - 1]
                nums[len(nums) - target_index - 1] = tmp
                break

        print(nums)


def main():
    s = Solution()
    s.nextPermutation([1, 2, 3, 5, 6, 4])


if __name__ == '__main__':
    main()
