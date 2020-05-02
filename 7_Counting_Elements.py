class Solution:
    def countElements(self, arr: List[int]) -> int:
        d = {}
        count = 0
        
        for i in arr:
            d[i] = d.get(i,0) + 1
        for i in arr:
            if i+1 in d and d[i] != 0:
                d[i] -= 1
                count += 1
        return count