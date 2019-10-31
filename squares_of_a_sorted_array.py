class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        solution = []
        for i, e in enumerate(A):
            solution.append(e**2)
        return sorted(solution)
    
"""
Runtime: 268 ms, faster than 57.46% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 15.6 MB, less than 5.95% of Python3 online submissions for Squares of a Sorted Array.
"""
