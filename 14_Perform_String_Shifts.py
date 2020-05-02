class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        cnt0 = cnt1 = 0
        
        for i in range(len(shift)):
            if shift[i][0] == 0:
                cnt0 += shift[i][1]
            else:
                cnt1 += shift[i][1]
        newstr = ''
        diff = abs(cnt0 - cnt1)
        diff %= len(s)
        
        if diff == 0:
            return s
        elif cnt1 > cnt0:
            return s[-diff:]+s[:-diff]
        else:
            return s[diff:]+s[:diff]