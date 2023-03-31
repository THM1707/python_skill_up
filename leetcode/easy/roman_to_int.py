class Solution:
    ROMAN_DICT = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def to_roman_value(self, c: str) -> int:
        return self.ROMAN_DICT[c]

    def roman_to_int(self, s: str) -> int:
        result = 0
        last_val = 0

        for i in range(len(s) - 1, -1, -1):
            cur_val = self.to_roman_value(s[i])

            if last_val > cur_val:
                result -= cur_val
            else:
                result += cur_val
            last_val = cur_val

        return result
