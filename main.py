def find_sum_for_n(n: int) -> int:
    _START = 5

    s = 0
    for i in range(n):
        s += (_START + i)

    return s


def main() -> None:
    print(find_sum_for_n(20))
    a = 3
    if a < (b := 10/3):
        print('too small')


if __name__ == '__main__':
    main()
