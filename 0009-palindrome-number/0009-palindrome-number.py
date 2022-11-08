class Solution:
    def isPalindrome(self, x: int) -> bool:
        if( x < 0):
            return False
        number = x
        reverse = 0
        while(number > 0):
            y = number % 10
            number = number//10
            reverse = reverse*10 + y
        return reverse == x
    
        