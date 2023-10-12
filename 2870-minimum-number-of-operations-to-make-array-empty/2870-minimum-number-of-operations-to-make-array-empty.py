class Solution:
    def minOperations(self, nums: List[int]) -> int:
        lst = Counter(nums)
        count=0
        print(lst)
        for i in lst.keys():
            if lst[i]==1:
                return -1
            print(lst[i])
            count+=(lst[i]+2)//3
        return count
        