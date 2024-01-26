from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        x = len(flowerbed)
        has_one = False
        consecutive_zero = 0

        for i in range(x):
            if flowerbed[i] == 0:
                consecutive_zero += 1
                continue

            n -= int(consecutive_zero / 2)
            consecutive_zero = 0
            has_one = True

        if n - int(consecutive_zero / 2) - (1 if not has_one else 0) > 0:
            return False

        return True


def main():
    s = Solution()
    assert s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1) == True
    assert s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2) == False
    assert s.canPlaceFlowers(flowerbed=[0, 0, 0, 0, 0], n=4) == False


if __name__ == '__main__':
    main()
