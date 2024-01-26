class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[gcd(len(str1), len(str2))]


def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)


def main():
    s = Solution()
    assert s.gcdOfStrings("ababab", "abab") == "ab"
    assert s.gcdOfStrings("abcabc", "abc") == "abc"
    assert s.gcdOfStrings("leet", "code") == ""


if __name__ == '__main__':
    main()
