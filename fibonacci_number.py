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
