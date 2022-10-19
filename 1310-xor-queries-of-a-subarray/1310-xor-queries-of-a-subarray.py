class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr)+1)
        for i in range(len(arr)):
            prefix[i+1] = prefix[i] ^ arr[i]
     
        final=[]
        for i,j in queries:
            final.append(prefix[i]^prefix[j+1])
        return final