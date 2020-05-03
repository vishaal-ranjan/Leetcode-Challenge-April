from collections import deque

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.q = deque()
        self.d = {}
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        
        if not self.q:  
            return -1
        while self.q and self.d[self.q[0]] >= 2:
            self.q.popleft()
        if self.q:
            return self.q[0]
        else:
            return -1

    def add(self, value: int) -> None:
        self.q.append(value)
        self.d[value] = self.d.get(value,0) + 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)