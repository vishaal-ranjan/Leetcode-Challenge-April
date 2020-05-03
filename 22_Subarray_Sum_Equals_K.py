class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        d[0] = 1
        current, final = 0, 0
        for i in nums:
            current += i
            if current-k in d:
                final += d[current-k]
            d[current] = d.get(current, 0) + 1
        return final