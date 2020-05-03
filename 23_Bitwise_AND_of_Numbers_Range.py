class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        answer = 0
        
        for bit in range(30, -1, -1):
            if m & (1<<bit) != n & (1<<bit):
                break
            else:
                answer |= (m & (1<<bit))
            
        return answer