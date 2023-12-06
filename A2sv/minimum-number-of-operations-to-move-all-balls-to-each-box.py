class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones_index=[]
        ans=[]
        for i in range(len(boxes)):
            if boxes[i]=="1":
                ones_index.append(i)
        print(ones_index)
        for i in range(len(boxes)):
            z=0
            for j in range(len(ones_index)):
                z+=(abs(i-ones_index[j]))
            ans.append(z)
        return ans