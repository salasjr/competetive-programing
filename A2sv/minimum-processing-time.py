class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        ans1=[]
        ans2=[]
        for i in range(3,len(tasks),4):
            ans1.append(tasks[i])
        for j in range(len(processorTime)-1,-1,-1):
            ans2.append(processorTime[j])
        ans=[]
        for i in range(len(ans1)):
            ans.append(ans1[i]+ans2[i])
        return max(ans)


        