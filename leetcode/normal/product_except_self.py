from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        prefixes = [1] * num_len
        suffixes = [1] * num_len
        result = []

        for i in range(1, num_len):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]

        for i in range(num_len - 2, -1, -1):
            suffixes[i] = suffixes[i + 1] * nums[i + 1]

        for i in range(num_len):
            result.append(prefixes[i] * suffixes[i])

        return result

def main():
    s = Solution()
    s.productExceptSelf([1,2,3,4])

if __name__ == '__main__':
    main()