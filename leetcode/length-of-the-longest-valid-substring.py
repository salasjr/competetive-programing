class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        max_length =0 
        right = len(word)-1

        for i in range(len(word)-1,-1,-1):
            for j in range(i,min(i+10,right+1)):
                if word[i:j+1] in forbidden_set:
                    right=j-1
                    break
            max_length=max(max_length,right-i+1)

        return max_length
        