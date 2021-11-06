class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, number in enumerate(nums):
            if target-number in seen:
                return([seen[target-number], i])
            else:
                seen[number] = i