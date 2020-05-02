from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            largest = -heapq.heappop(stones)
            second = -heapq.heappop(stones)  
            if largest > second:
                heapq.heappush(stones, -(largest - second))
            elif len(stones) == 0:
                heapq.heappush(stones, 0)
                
        return -stones[0]