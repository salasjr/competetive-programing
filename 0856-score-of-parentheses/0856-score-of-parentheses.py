class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(score)
                score = 0
            else:
                last_score = stack.pop()
                score = last_score + max(2 * score, 1)

        return score
        
        