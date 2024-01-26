# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

class Solution:
    VOWELS = ['a', 'i', 'u', 'e', 'o']

    def findTheLongestSubstring(self, s: str) -> int:
        vowels_dict = {
            'a': 0,
            'i': 0,
            'u': 0,
            'e': 0,
            'o': 0
        }

        most_left_index = 0
        most_right_index = 0

        for i, c in enumerate(s):
            if c in vowels_dict:
                vowels_dict[c] += 1
            if most_left_index == 0 and i != 0:
                most_left_index = i
            if most_right_index < i:
                most_right_index = i

        if all(x % 2 == 0 for x in vowels_dict.values()):
            return len(s)
