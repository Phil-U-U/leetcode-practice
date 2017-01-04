'''
Time: O(nlogn)


    10
    / \
   5  15
  / \   \ 
 1   8   7

   5  
  / \   
 1   8

Reference: 
    http://www.cnblogs.com/grandyang/p/5188938.html
    Above also gives O(n) solution

 Author: Phil H. Cui
 Date: 01/04/2017
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__( self ):
        self.res = 0

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.dfs( root )
        return self.res

    # DFS in the way that left -> left -> ..., but here it combines BFS
    def dfs( self, root ):    
        # base case
        if not root:
            return

        # Similar to valid-binary-search-tree, but different
        d = self.countBFS( root, float("-inf"), float("inf") )
           
        # if d is not -1, which means a valid BST has been found,
        # then replace res by d/the maximum of (res, d)
        if d != -1:
            self.res = max( self.res, d )
            return 

        # if d is -1, then check if root.left is valid BST, 
        # it goes into this function itself, 
        # if is a valid BST,
        # replace res by d/the maximum of (res, d)
        # else check the right branch of current tree root
        # since the right branch may have a larger BST than the left branch 
        # use max(res, d) to replace res for simple and coherent code.
        self.dfs( root.left )
        self.dfs( root.right )

    # BFS in the sense that first left and then right,
    # also it combines DFS ( middle -> left -> right ... )
    def countBFS( self, root, low, high ):  
        if not root:
            return 0

        # From now on, any of the following three conditions are not satisfied,
        # which means, looking from the current node "root",   
        # the tree is not a valid binary search tree (its subtree may be, not the whole)
        # and return -1 as both the label and the computational easiness.   

        if root.val < low or root.val > high:   # not a binary search tree
            return -1    # gaurantee the fastest speed to return when invalid BST is found. 

        left = self.countBFS( root.left, low, root.val )
        if left == -1:
            return -1  # gaurantee the fastest speed to return when invalid BST is found.  

        right = self.countBFS( root.right, root.val, high )    
        if right == -1:
            return -1   # gaurantee the fastest speed to return when invalid BST is found. 

        # if a BST is found, count the total number of nodes: 
        # 1(root) + N(nodes in left branch) + N(nodes in right branch)
        # the base case is 0, then leaf for 1, and then increases as index 
        # of layers increases. 
        return 1 + left + right 
        


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)

    root.right = TreeNode(15)
    root.right.right = TreeNode(7)
    print Solution().largestBSTSubtree(root)