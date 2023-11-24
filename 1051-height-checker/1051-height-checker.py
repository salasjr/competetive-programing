class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        checker=sorted(heights)
        count=0
        for i in range(len(heights)):
            if checker[i]!=heights[i]:
                count+=1
        return count
        