'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

Example of valid binary search tree:
(All left nodes must be less than root;
 All right nodes must be greater than root )
         10
       /    \
      5      15
     / \     /  \         low, high
    2   8   12   20     8: [5,   10]
       / \
      7   9            7: [5, 8]  ;  9: [8, 10]

Author: Phil H. Cui
Date: 12/31/16

'''
# DFS: middle -> left -> right
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def helper( self, root, low, high ):

        if not root:
            return True

        return low < root.val and root.val < high \
            and self.helper( root.left, low, root.val ) \
            and self.helper( root.right, root.val, high )


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        low, high = float("-inf"), float("inf")

        return self.helper( root, low, high )





if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print 'Expected:{} - Calculated: {}'.format( 'True', Solution().isValidBST( root ) )

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print 'Expected:{} - Calculated: {}'.format( 'False', Solution().isValidBST( root ) )
