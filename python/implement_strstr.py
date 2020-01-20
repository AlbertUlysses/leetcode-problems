class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
"""
Runtime: 24 ms, faster than 99.83% of Python3 online submissions for Implement strStr().
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement strStr().
"""
