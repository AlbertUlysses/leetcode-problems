class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True 
        nothappy = []
        while n != 1:
            origin = n
            num = 0
            while n > 9:
                temp = n % 10
                n = n//10
                num = temp**2 + num
            n = n**2 + num
            nothappy.append(origin)
            if n in nothappy:
                return False
        return True

