#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?


Author: Phil H. Cui
Date: 01/04/2017

'''

# from heapq import heappush, heappop
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        res, d = [], deque()
        curMax, curMax2 = float("-inf"), float("-inf")

        for x in nums[:k]:
        	
        	d.append(x)
        	if x > curMax:
        		curMax, curMax2 = x, curMax
        		
        	elif x > curMax2:
        		curMax2 = x

        res.append(curMax)

        for i, x in enumerate( nums[k:] ):	
        	if d.popleft() == curMax:
        		curMax = curMax2

        		

        	if x > curMax:
        		res.append(x)
        		curMax = x
        	else:
        		res.append(curMax)	
        	

        return res	

if __name__ == "__main__":
	nums, k = [1,  3,  -1,  -3,  5,  3,  6,  7], 3
	print Solution().maxSlidingWindow( nums, k )