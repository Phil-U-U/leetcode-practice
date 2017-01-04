#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Time:  O(m * n)
Space: O(m * n)
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

Reference: 
http://www.cnblogs.com/grandyang/p/4402656.html
https://segmentfault.com/a/1190000003753307


Author: Phil H. Cui
Date: 01/03/2017

'''


# DFS: 从边缘开始，向周围（上下左右）探索，直到走到岸边（碰到0），返回岛上陆地，
# 再次向周围（上下左右）搜索，
# 直到四面八方所有的探子都回来（return）后，表明发现了一个孤岛（cnt＋1）
# 

class Solution(object):


	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		if not grid:
			return 0
		
		self.nrows, self.ncols = len(grid), len(grid[0])	

		used = [[False for _ in xrange(self.ncols)] for _ in xrange(self.nrows)]

		cnt = 0

		for i in xrange(self.nrows):
			for j in xrange(self.ncols):
				if grid[i][j] == '1' and not used[i][j]:
					self.dfs( grid, used, i, j )
					cnt += 1
		return cnt		

	def dfs( self, grid, used, i, j):
		if grid[i][j] == '0' or used[i][j]:
			return 
		used[i][j] = True		

		if i != 0:
			self.dfs( grid, used, i-1, j)  # up
		if i != self.nrows-1:
			self.dfs( grid, used, i+1, j)  # down
		if j != 0:
			self.dfs( grid, used, i, j-1)  # left
		if j != self.ncols-1:
			self.dfs( grid, used, i, j+1)  # right


class Solution_2:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if not grid:
            return 0
    
        row = len(grid)
        col = len(grid[0])
        used = [[False for j in xrange(col)] for i in xrange(row)]
    
        count = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1' and not used[i][j]:
                    self.dfs(grid, used, row, col, i, j) # finish one dfs search means an island has been found.
                    count += 1
        return count

    def dfs(self, grid, used, row, col, x, y):
        if grid[x][y] == '0' or used[x][y]:
            return
        used[x][y] = True
    
        if x != 0:
            self.dfs(grid, used, row, col, x - 1, y)  # up
        if x != row - 1:
            self.dfs(grid, used, row, col, x + 1, y)  # down
        if y != 0:
            self.dfs(grid, used, row, col, x, y - 1)  # left
        if y != col - 1:
            self.dfs(grid, used, row, col, x, y + 1)  # right



if __name__ == "__main__":
	grid = ["11110", "11010", "11000", "00000"]
	print Solution().numIslands( grid )       