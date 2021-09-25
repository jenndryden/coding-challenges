class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in nums: 
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        for i in seen:
            if seen[i] == 1:
                return i