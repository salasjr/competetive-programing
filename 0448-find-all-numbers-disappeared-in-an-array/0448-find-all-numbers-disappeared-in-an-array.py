class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        mydict = {}
        for num in nums:
            mydict[num] = True
        miss_num=[]
        for i in range(1, len(nums)+1):
            if i not in mydict:
                miss_num.append(i)
        return miss_num
            
        