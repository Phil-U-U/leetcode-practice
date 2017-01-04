'''

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

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
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []

        res, cur_level = [], [root]

        while cur_level:
            nodesThisLayer, next_level = [], []
            for node in cur_level:
                # print node.val

                nodesThisLayer.append(node.val)
                # print nodesThisLayer
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            # print cur_level
            res.append(nodesThisLayer)
            cur_level = next_level

        return res


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print Solution().levelOrder( root )
