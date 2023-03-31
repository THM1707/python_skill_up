# https://leetcode.com/problems/bag-of-tokens/
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0

        if not tokens:
            return score

        tokens.sort()

        if tokens[0] > power:
            return score

        score = len(tokens)

        summarize = sum(tokens) + power

        for i in range(len(tokens) - 1, -1, -1):
            score -= 2
            if power + tokens[i] >= summarize - power - tokens[i]:
                if power >= summarize - power - tokens[i]:
                    score += 1
                    break

                break

            power += tokens[i]

        return max(score, 1)

if __name__ == '__main__':
    print(Solution().bagOfTokensScore([68,85,34,25,60], 44))
