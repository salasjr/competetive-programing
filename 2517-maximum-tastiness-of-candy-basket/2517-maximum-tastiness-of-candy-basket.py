class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)
        price.sort()
        print(price[-1])
        l, r, ans = 0,price[-1], price[-1]
        while l <= r:
            mid = (l + r) // 2
            cntOfCandies, last = 1, price[0]

            for i in range(1, n):
                if price[i] - last >= mid:
                    cntOfCandies += 1
                    last = price[i]

            if cntOfCandies >= k:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans

        
        