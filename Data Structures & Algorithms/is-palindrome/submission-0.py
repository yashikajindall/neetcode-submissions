class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        reverse = s[::-1]
        if s == reverse:
            return True
        else:
            return False
