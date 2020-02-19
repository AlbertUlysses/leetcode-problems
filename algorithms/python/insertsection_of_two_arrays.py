# This code is wrong, work in progress
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        _list = []
        for i in nums2:
            if i in _list:
                pass
            else:
                low = 0
                high = len(nums1) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if i == nums1[mid]:
                        _list.append(i)
                    elif i < nums1[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
        return _list
