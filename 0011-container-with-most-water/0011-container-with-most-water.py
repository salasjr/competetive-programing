class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        left,right = 0,len(height)-1
        while left < right:
            height1 = min(height[left], height[right])
            width= right-left
            area = height1*width
            ans = max(area,ans)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans
            
        