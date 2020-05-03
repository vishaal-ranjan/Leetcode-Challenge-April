class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<=1:
            return True
        can_reach = 0
        i = 0
        
        while i <= can_reach:
            if i == n-1:
                return True
            can_reach = max(can_reach, i+nums[i])
            i += 1
            
        return False