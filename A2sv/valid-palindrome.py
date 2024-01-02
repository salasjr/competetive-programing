class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(s) - 1
        print(s)
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
