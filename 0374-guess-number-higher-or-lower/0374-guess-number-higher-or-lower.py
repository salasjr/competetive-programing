# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        r=n
        while l <=r:
            m = l + (r-l)//2
            print(m)
            if guess(m) == 0:
                return m
            if guess(m) == -1:
                print("jer")
                r = m-1
            if guess(m) ==1:
                print("jer2")
                l = m+1
        return m
                
        