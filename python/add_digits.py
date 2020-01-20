class Solution:
    def addDigits(self, num: int) -> int:
        def add_(int_):
            str_ = str(int_)
            list_ = []
            for i, e in enumerate(str_):
                list_.append(int(e))
            temp = sum(list_)
            if temp > 9:
                temp = add_(temp)
            return temp
        return add_(num)
"""
Runtime: 44 ms, faster than 25.85% of Python3 online submissions for Add Digits.
Memory Usage: 14.1 MB, less than 5.26% of Python3 online submissions for Add Digits.
"""
