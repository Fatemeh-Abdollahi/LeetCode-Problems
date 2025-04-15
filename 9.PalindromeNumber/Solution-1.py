class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reversedx = x[::-1]
        if x == reversedx:
            return True
        else:
            return False
        