class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def canBreak(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            for word in wordDict:
                if s.startswith(word, start) and canBreak(start + len(word)):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return canBreak(0)
        