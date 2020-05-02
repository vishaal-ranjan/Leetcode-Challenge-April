class Solution:
    def isHappy(self, n: int) -> bool:
        iters = 0
        while True:
            res = 0
            iters += 1
            if iters == 10:
                return False
            num = str(n)
            for i in range(len(num)):
                res += int(num[i])**2
                if res == 1 and i == len(num) - 1:
                    return True
            n = res