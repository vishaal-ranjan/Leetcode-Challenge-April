class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = collections.defaultdict(list)
        
        for i in strs:
            letters = tuple(sorted(i))
            sol[letters].append(i)
        return sol.values()