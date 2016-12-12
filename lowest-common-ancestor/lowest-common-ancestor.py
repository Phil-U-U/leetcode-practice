'''
Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree. According to the definition
of LCA on Wikipedia: "The lowest common ancestor is defined
between two nodes v and w as the lowest node in T that has
both v and w as descendants (where we allow a node to be a
descendant of itself)."

        _______3______
       /              \
    ___5__          ___1__
   /      \        /       \
   6      _2_      0        8
         /   \
        7    4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant
of itself according to the LCA definition.

Author: Phil H. Cui
Date: 12/05/16

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lowestCommonAncestor_1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base case (also case 1)
        if root in (None, p, q):
            return root

        searchLeft = self.lowestCommonAncestor( root.left, p, q )
        searchRight = self.lowestCommonAncestor( root.right, p, q )

        # Case 2: if p, q exist in both branches, return root
        if searchLeft != None and searchRight != None:
            return root

        # Case 3: if one of the branches returns None, continue to search the other branch
        if searchLeft == None:
            return searchRight
        else:
            return searchLeft

    def lowestCommonAncestor(self, root, p, q):
        if root in ( None, p, q):
            return root

        searchLeft, searchRight = [self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right)]

        return root if searchLeft and searchRight else searchLeft or searchRight

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print Solution().lowestCommonAncestor_1( root, TreeNode(5), TreeNode(1) )
    print Solution().lowestCommonAncestor_1( root, TreeNode(5), TreeNode(4) )
