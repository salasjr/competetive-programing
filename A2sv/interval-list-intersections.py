class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        ans = []
        while r < len(secondList) and l < len(firstList):
            a, b = firstList[l][0],firstList[l][1]
            c, d = secondList[r][0],secondList[r][1]
            x = max(a, c)
            y = min(b, d)
            if x <= y:  
                ans.append([x, y])
            if b < d:
                l += 1
            else:
                r += 1  
        return ans
       