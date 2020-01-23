class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        list_ = []
        while x:
            list_.append(x%10) 
            x = x//10
        return list_ == list_[::-1]
"""
Runtime: 92 ms, faster than 16.39% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
"""
