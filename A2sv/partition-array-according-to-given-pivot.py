class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before=[]
        after=[]
        number=[]
        for i in nums:
            if i>pivot:
                after.append(i)
            elif i<pivot:
                before.append(i)
            else:
                number.append(i)
        return before+number+after
                
        