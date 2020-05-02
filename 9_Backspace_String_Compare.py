class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a = []
        b = []
        for i in S:
            if i != '#':
                a.append(i)
            elif a:
                del a[-1]
                
        for i in T:
            if i != '#':
                b.append(i)
            elif b:
                del b[-1]
        return a == b