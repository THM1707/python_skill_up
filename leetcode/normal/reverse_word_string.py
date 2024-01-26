# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(x for x in reversed(s) if x)



assert Solution().reverseWords("the sky is blue") == "blue is sky the"
assert Solution().reverseWords("  hello world  ") == "world hello"
