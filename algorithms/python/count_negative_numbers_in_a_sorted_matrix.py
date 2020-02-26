class Solution:
    def countNegatives(self, grid) -> int:
        neg_count = 0
        for row in range(len(grid)):
            list_ = grid[row]
            count = 0
            if list_[0] < 0:
                neg_count += len(list_)
                count += 1
            low = 0
            high = len(list_) - 1
            while low <= high and count == 0:
                mid = (low + high) // 2
                if list_[mid + 1] < 0 and list_[mid] >= 0:
                    neg_count +=  len(list_[mid+1:])
                    count += 1
                elif list_[mid] >= 0:
                    low = mid + 1
                else:
                    high =  mid - 1
        return count 


list_ = [[8,-2,-2,-2,-4,-5,-5],[-2,-3,-3,-4,-4,-5,-5],[-2,-5,-5,-5,-5,-5,-5],[-3,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5],[-5,-5,-5,-5,-5,-5,-5]]

list_2 = [5, 4, 3]

test = Solution()
test2 = Solution()

print(test.countNegatives(list_))
#print(test.count_neg(list_2))
