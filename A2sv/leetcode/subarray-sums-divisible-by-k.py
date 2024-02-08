class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        arr = [0] * k
        total_sum = 0
        for num in nums:
            total_sum += num
            total_sum %= k
            total_sum = (total_sum + k) % k  
            arr[total_sum] += 1
        count = arr[0]  
        for i in range(len(arr)):
            count += (arr[i] * (arr[i] - 1)) // 2
        return count