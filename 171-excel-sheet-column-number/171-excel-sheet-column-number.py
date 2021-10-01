class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        multiplier = 1
        output = 0 
        for i in range(len(columnTitle)-1,-1,-1):
            output += (ord(columnTitle[i])-64) * multiplier
            multiplier *= 26
        return output