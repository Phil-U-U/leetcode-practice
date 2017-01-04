#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Time:  O(n * 2^n)
Space: O(1)

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Reference:

http://bangbingsyb.blogspot.com/2014/11/leetcode-subsets-i-ii.html

起始subset集为：[]
添加S0后为：[], [S0]
添加S1后为：[], [S0], [S1], [S0, S1]
添加S2后为：[], [S0], [S1], [S0, S1], [S2], [S0, S2], [S1, S2], [S0, S1, S2]
红色subset为每次新增的。显然规律为添加Si后，新增的subset为克隆现有的所有subset，并在它们后面都加上Si。

Author: Phil H. Cui
Date: 01/03/2017
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
        	return [nums]

        cur = []

        return self.recur( cur, sorted(nums) )


    def recur( self, cur, nums):    
		if not nums:
			return  [cur]

		# 加 nums[0] 之前， 所有的组合 ＋ 加 nums[0] 之后，所有的组合， 见上面的解释
		return self.recur( cur, nums[1:] ) + self.recur( cur+[nums[0]], nums[1:] )



if __name__ == "__main__":
    print Solution().subsets([1, 2, 3])