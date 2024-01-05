from typing import Optional


def binary_search(arr: list[int], n: int) -> Optional[int]:
    i, j = 0, len(arr) - 1
    while i <= j:
        k = int((i + j) / 2)
        if arr[k] == n:
            return k
        elif n < arr[k]:
            j = k - 1
        else:
            i = k + 1
    return None


def main():
    print(binary_search([1, 4, 9, 12, 21, 45, 50], 9))
    print(binary_search([1, 4, 9, 12, 21, 45, 50], 10))
    print(binary_search([1, 4, 9, 12, 21, 45, 50], 12))


if __name__ == '__main__':
    main()
