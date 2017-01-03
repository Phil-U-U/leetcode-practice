'''
Time:  O(m * n)
Space: O(m + n)

Given a m x n grid filled with non-negative numbers, find a path from 
top left to bottom right which minimizes the sum of all numbers 
along its path.

Note: You can only move either down or right at any point in time.

Reference: http://www.davex.pw/2016/01/20/LeetCode-Minimum-Path-Sum/

Author: Phil H. Cui
Date: 01/03/2017

'''

class Solution(object):
    def minPathSum(self, grid):
		"""
        :type grid: List[List[int]]
        :rtype: int
        """
		n_rows, n_cols = len( grid ), len( grid[0] )

		for i in xrange(1, n_rows):
			grid[i][0] += grid[i-1][0]

		for j in xrange(1, n_cols):
			grid[0][j] += grid[0][j-1]

		for i in xrange(1, n_rows):
			
			for j in xrange(1, n_cols):

				grid[i][j] += min( grid[i][j-1], grid[i-1][j] )


		return grid[n_rows-1][n_cols-1]  		



if __name__ == "__main__":
	# grid = [[0,1], [1,0]]
	# print Solution().minPathSum( grid )        
	grid = [[1,3,1],[1,5,1],[4,2,1]]
	print Solution().minPathSum( grid )