"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
"""
        # TODO: write for-loop for each row in matrix
        # TODO: implement binary search on each list that finds the point where it is greater than 0
        # target here is always 0, as oppossed to normal binary search
        # return the remainder leng
class Solution:
    def count_neg(self, list_: list) -> int:
        low = 0
        high = len(list_) - 1
        while low < high:
            mid = (low + high) // 2
            if list_[mid + 1] < 0 and list_[mid] >= 0:
                return len(list_[mid+1:])
            elif list_[mid] >= 0:
                low = mid + 1
            else:
                high =  mid - 1
        return 0

list_ = [5, 4, 0, -1, -1, -2]
list_2 = [5, 4, 3]

test = Solution()
test2 = Solution()

print(test.count_neg(list_))
print(test.count_neg(list_2))
