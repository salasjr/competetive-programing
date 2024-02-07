class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = [0]
        for num in nums:
            self.arr.append(self.arr[-1] + num)
        print(self.arr)

    def sumRange(self, left: int, right: int) -> int:
        z=self.arr[right+1]-self.arr[left]
        return z
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)