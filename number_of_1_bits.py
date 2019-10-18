class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        bin_ = bin(n)
        for i, e in enumerate(bin_):
            if e == '1':
                count += 1
        return count
"""
Runtime: 20 ms, faster than 50.95% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.8 MB, less than 45.00% of Python online submissions for Number of 1 Bits."""
"""Alternatively we can use some more of the built in functions that is slightly faster."""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
"""
Runtime: 16 ms, faster than 77.94% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.9 MB, less than 7.50% of Python online submissions for Number of 1 Bits."""
