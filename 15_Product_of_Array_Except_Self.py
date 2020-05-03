class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, output = [1]*len(nums), [1]*len(nums), [1]*len(nums)
        left[0] = 1
        right[len(nums) - 1] = 1
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        for i in reversed(range(len(nums) -1)):
            right[i] = right[i+1]*nums[i+1]
        for i in range(len(nums)):
            output[i] = left[i]*right[i]
            
        return output