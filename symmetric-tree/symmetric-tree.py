
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive solution
class Solution_1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.symmetricHelper( root.left, root.right )

    def symmetricHelper( self, left, right  ):
        if left is None and right is None:
            return True
        elif left is None or right is None or left.val != right.val:
            return False
        else:# left.val == right.val:
            return self.symmetricHelper( left.left, right.right ) and self.symmetricHelper( left.right , right.left )

# Iterative solution
class Solution( object ):
    def isSymmetric( self, root ):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        stack = []
        stack.append( root.left )
        stack.append( root.right )

        while stack:
            p, q = stack.pop(), stack.pop()

            if p is None and q is None:
                continue
            elif p is None or q is None or p.val != q.val:
                return False
            else:
                stack.append(p.left)
                stack.append(q.right)
                stack.append(p.right)
                stack.append(q.left)

        return True



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    # root.left.right.left = TreeNode(7)
    # root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print Solution_1().isSymmetric(root)
    print Solution().isSymmetric(root)
