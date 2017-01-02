#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
# Time:  O(2^n)
# Space: O(1)

The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

Example: 
例举grey code序列，并找规律 :
n = 0: 0
n = 1: 0, 1
n = 2: 00, 01, 11, 10  (0, 1, 3, 2)
n = 3: 000, 001, 011, 010, 110, 111, 101, 100 (0, 1, 3, 2, 6, 7, 5, 4)
以n = 3为例，grey code中前4个包括了n = 2的所有gray code。后4个则是前4个逆序后加上2^2。

推广：n = i的grey code的前一半包括了n = i-1的所有grey code，而后一半则为前一半逆序后家上2^(i-1)。

Author: Phil H. Cui
Date: 1/2/2017

'''
class Solution():
	def grayCode( self, n ):

		res = [0]

		for i in xrange(n):

			for x in reversed(res):
				res.append( 1 << i | x )

		return res		


if __name__ == "__main__":
    print Solution().grayCode(0)
    print Solution().grayCode(2)    
    print Solution().grayCode(3)      
