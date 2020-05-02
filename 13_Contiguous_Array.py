class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_oc = {}
        first_oc[0] = 0
        pref = 0
        solution = 0
        
        for i in range(len(nums)):
            pref += 1 if nums[i] == 1 else -1
            if pref in first_oc:
                solution = max(solution, i + 1 - first_oc[pref])
            else:
                first_oc[pref] = i+1
        
        return solution