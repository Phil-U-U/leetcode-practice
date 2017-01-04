#!/usr/bin/env python
# -*- coding: utf-8 -*- 


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

	def __init__(self):
		self.res = 0

	def largestBSTSubtree( self, root ):

		self.traverse(root)
		return self.res

	# traverse 被调用时，从root开始重新看整个tree。
	# 就是遍历
	# DP
	def traverse( self, root ): 
		
		d = self.cntValidBST( root, float("-inf"), float("inf") )

		if d != -1:
			# in case the root tree itself is not valid BST, but both left and right branches are, find their maximum
			self.res = max( self.res, d )  
			return 

		# if whole tree is invalid
		# traverse left first
		self.traverse( root.left )
		# In the end, traverse right
		self.traverse( root.right )

	# validate BST and count the number of nodes at the same time
	# 一旦发现invalid tree, 及时返回
	# DFS
	def cntValidBST( self, root, low, high ):  

		if not root:
			return 0

		if low > root.val or root.val > high:
			return -1

		left = self.cntValidBST( root.left, low, root.val )	
		if left == -1:
			return -1

		right = self.cntValidBST( root.right, root.val, high )
		if right == -1:
			return -1

		return 1 + left + right



if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)

    root.right = TreeNode(15)
    root.right.right = TreeNode(7)
    print Solution().largestBSTSubtree(root)