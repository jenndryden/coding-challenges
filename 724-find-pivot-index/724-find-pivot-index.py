class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if right_sum - num == left_sum:
                return i
            right_sum -= num
            left_sum += num
        return -1
                