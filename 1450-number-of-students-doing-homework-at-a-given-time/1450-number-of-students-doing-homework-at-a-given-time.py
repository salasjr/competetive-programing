class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans=0
        for i in range(len(startTime)):
            a=startTime[i]
            b=endTime[i]
            if b>=queryTime and a<=queryTime:
                ans+=1
        return ans