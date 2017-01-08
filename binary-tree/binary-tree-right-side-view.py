#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
# Time:  O(n)
# Space: O(h)
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

Reference:
http://blog.csdn.net/bruce128/article/details/50698294
http://bookshadow.com/weblog/2015/04/03/leetcode-binary-tree-right-side-view/
求一棵二叉树的右视图。用BFS的方式遍历二叉树，取每层的最后一个节点。


Author: Phil H. Cui
Date: 01/03/2017

'''
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def rightSideView(self, root):
		"""
        :type root: TreeNode
        :rtype: List[int]
        """
		# DFS
		res, depth = [], 1

		self.rightSideView_DFS( root, depth, res )

		return res

	def rightSideView_DFS( self, node, depth, res ):


		if not node:
			return

		if depth > len(res):  # only one node is peeked at each layer
			res.append(node.val)

		self.rightSideView_DFS( node.right, depth+1, res )
		self.rightSideView_DFS( node.left,  depth+1, res )					



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    result = Solution().rightSideView(root)
    print result