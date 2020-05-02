class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = float('-inf')
        for i,v in enumerate(nums):
            if i == 0:
                curr_sum = v
            else:
                curr_sum += v
            curr_sum = max(curr_sum, v)
            max_sum = max(max_sum, curr_sum)
        return max_sum