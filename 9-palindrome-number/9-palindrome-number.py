class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        divider = 1
        
        while x >= 10 * divider:
            divider *= 10
            
        while x:
            if (x // divider) != x % 10:
                return False
            x = (x % divider) // 10
            divider = divider / 100 
        return True