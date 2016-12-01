'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

Return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
Author: Phil H. Cui
Date: 11/30/16

'''


class TreeNode( object ):
    def __init__( self, x ):
        self.val = x
        self.left = None
        self.right = None

class Solution( object ):
    def levelOrderTraverse( self, root ):
        # BFS, Queue

        if root is None:
            return []

        res, queue = [], [root]

        res.append( [root.val] )

        while queue:
            node = queue.pop(0)

            temp = []
            if node.left is not None:
                temp.append(node.left.val)
                queue.append( node.left )
            # else:
            #     temp.append('Null')
            if node.right is not None:
                temp.append(node.right.val)
                queue.append( node.right)
            # else:
            #     temp.append('Null')
            if len(temp) > 0:
                res.append(temp)

        return res

    def levelOrder( self, root ):
        if root is None:
            return []

        res, current = [], [root]
        while current:
            next_level, vals = [], []

            for node in current:
                vals.append(node.val)

                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)

            current = next_level

            res.append( vals )

        return res

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print Solution().levelOrderTraverse(root)
