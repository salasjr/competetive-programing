class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ans1=""
        ans2=""
        for i in range(len(word1)):
            ans1+=word1[i]
        for i in range(len(word2)):
            ans2+=word2[i]
        return ans1==ans2
        