class Solution:
    def countNegatives(self, grid) -> int:
        neg_count = 0
        for row in range(len(grid)):
            list_ = grid[row]
            count = None 
            if list_[0] < 0:
                neg_count += len(list_)
                count = 1
            if list_[-1] >= 0:
                count = 1
            low = 0
            high = len(list_) - 1
            while low <= high and count is None:
                mid = (low + high) // 2
                if list_[mid + 1] < 0 and list_[mid] >= 0:
                    neg_count +=  len(list_[mid+1:])
                    count = 1
                elif list_[mid] >= 0:
                    low = mid + 1
                elif list_[mid] < 0:
                    high =  mid - 1
        return neg_count 

"""
Runtime: 124 ms, faster than 81.93% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
"""
