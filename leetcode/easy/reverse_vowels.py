# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    VOWELS = ["a", "e", "i", "o", "u"]

    def reverseVowels(self, s: str) -> str:
        r = ""
        vowels = []

        for c in s:
            if c.lower() in self.VOWELS:
                vowels.append(c)

        for c in s:
            if c.lower() in self.VOWELS:
                r += vowels.pop()
            else:
                r += c
        return r


def main():
    s = Solution()
    assert s.reverseVowels("hello") == "holle"
    assert s.reverseVowels("leetcode") == "leotcede"


if __name__ == '__main__':
    main()
