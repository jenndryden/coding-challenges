class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while True: 
            if n in seen:
                break
            counter = 0
            for i in range(len(str(n))):
                counter += int(str(n)[i]) ** 2
            seen[n] = 1
            n = counter
            counter = 0
            if n == 1:
                return True
                break
            else:
                continue
        return False
                