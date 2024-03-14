class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def good(capacity):
            total_weight=0
            t=1

            for w in weights:
                total_weight+=w
                if total_weight>capacity:
                    t+=1
                    total_weight=w
            return t>days
        low,high=max(weights),sum(weights)

        while low < high:
            capacity=low + (high-low)//2

            if good(capacity):
                low=capacity+1
            else:
                high=capacity
        return low
        