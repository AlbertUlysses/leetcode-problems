# The solution runs at O(nlogn) it can be improved 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        _list = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        for i in nums2:
            if i not in _list:
                low = 0
                high = len(nums1) - 1
                while low <= high and i not in _list:
                    mid = (low + high) // 2
                    if i == nums1[mid]:
                        _list.append(i)
                    elif i < nums1[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
        return _list
"""
Runtime: 84 ms, faster than 6.90% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays.
"""
