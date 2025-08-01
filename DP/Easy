"""
118. Pascal's Triangle
Difficulty: Easy
Tags: Array, Dynamic Programming
URL: https://leetcode.com/problems/pascals-triangle/
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[]] * numRows

        for i in range(numRows):
            triangle[i] = [1] * (i + 1)
            for j in range(1, i//2 + 1):
                # Using the pattern of the fact it mirrors
                triangle[i][j] = triangle[i][i - j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        return triangle
