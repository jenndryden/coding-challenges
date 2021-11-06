class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curr_sum = 0
        
        for n in nums:
            if curr_sum<0:
                curr_sum = 0
            curr_sum += n
            maxSub = max(maxSub, curr_sum)
        return maxSub