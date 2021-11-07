class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        
        divider = 1
        
        while x >= divider * 10:
            divider *= 10
            
        while x:
            if x % 10 != x // divider:
                return False
            x = x % divider 
            x = x // 10
            divider = divider / 100
        return True 