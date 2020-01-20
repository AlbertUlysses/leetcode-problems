"""Solution without using recursion"""
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            curr_sum = 1
            prev_sum = 0
            for num in range(2, N+1):
                ans = curr_sum + prev_sum
                prev_sum = curr_sum
                curr_sum = ans
            return ans
"""Runtime: 48 ms, faster than 30.43% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.9 MB, less than 5.80% of Python3 online submissions for Fibonacci Number."""
"""solution with recursion"""
class Solution:
    def fib(self, N: int) -> int:
        if N<=1:
            return N
        else:
            return(self.fib(N - 1) + self.fib(N - 2))
"""Runtime: 1080 ms, faster than 19.93% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.9 MB, less than 5.80% of Python3 online submissions for Fibonacci Number."""
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return N
        last: int = 0
        next: int = 1
        for _ in range(1, N):
            last, next = next, last + next
        return next
"""
Runtime: 36 ms, faster than 74.78% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
"""
