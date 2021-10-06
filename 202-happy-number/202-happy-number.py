class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:

                #helper function
                #add to set 
            visit.add(n)
            n = self.helperFunction(n)

                #return true if 1
            if n == 1:
                return True

                #otherwise return false
        return False
        
    def helperFunction(self, n: int) -> int:
        count = 0 
            
        while n != 0:
            digit = n % 10
            count += digit ** 2
            n = n // 10
        return count