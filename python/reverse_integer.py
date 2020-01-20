class Solution:
    def reverse(self, x: int) -> int:
        
        temp = x
        if x < 0:
            temp = x * -1
        str_ = str(temp)
        ans = ''
        for e in str_:
            ans = e + ans
            str_ = str_[:-2]
        ans = int(ans)
        if x < 0:
            ans = -1 * ans
        if (ans < (-2**31)) or (ans > (2**31)-1):
            return 0 
        return ans

"""Runtime: 40 ms, faster than 60.07% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.1 MB, less than 5.26% of Python3 online submissions for Reverse Integer."""
