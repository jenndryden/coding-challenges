class Solution:
    def reverse(self, x: int) -> int:
        neg  = False
        if x < 0:
            neg = True
        y = str(abs(x))
        z = int(y[::-1])
        if z > 2**31 or z < 2**-31 -1:
            return 0 
        if neg:
            z = z*-1
            if z > 2**31 or z < 2**-31 -1:
                return z
        return z