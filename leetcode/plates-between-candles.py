class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        for i in range(len(s)):
            if s[i] == '|': candles.append(i)

        run=[]
        summ=0
        for i in range(len(s)):
            if s[i]=="*":
                summ+=1
            run.append(summ)
        res = []
        for qleft, qright in queries:
            left_pos, right_pos = -1, -1
            
            left, right = 0, len(candles)-1
            while left <= right:
                mid = (left+right) // 2
                if candles[mid] >= qleft:
                    right = mid - 1
                    left_pos = mid
                else:
                    left = mid + 1
            left, right = 0, len(candles)-1
            while left <= right:
                mid = (left+right) // 2
                if candles[mid] <= qright:
                    left = mid + 1
                    right_pos = mid
                else:
                    right = mid - 1
            if (left_pos != -1) & (right_pos!= -1) & (right_pos > left_pos):
                res.append((candles[right_pos] - candles[left_pos]) - (right_pos - left_pos))
            else:
                res.append(0)
        return res

                