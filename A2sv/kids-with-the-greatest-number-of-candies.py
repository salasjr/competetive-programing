class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=sorted(candies)
        ans=[]
        for i in candies:
            if i+extraCandies >= a[-1]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        