'''
Given a nested list of integers, return the sum of all integers in the list weighted by
their depth.
Each element is either an integer, or a list -- whose elements may also be integers
or other lists.
Example 1: Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at
depth 1)
Example 2: Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2,
and one 6 at depth 3; 1 + 8 + 18 = 27)


Author: Phil H. Cui
Date: 12/01/16

'''
class Solution(object):
    # DFS, Recursion
    def calcSum( self, l, depth = 1 ):
        res = 0
        for ele in l:
            if type(ele) == int:
                res += ele * depth
            elif type(ele) == list:
                res += self.calcSum( ele, depth + 1 )
        return res


if __name__ == "__main__":
    l1 = [[1,1],2,[1,1]]
    l2 = [1,[4,[6]]]
    solution = Solution()
    print "{}-{}".format(10, solution.calcSum(l1) )
    print "{}-{}".format(27, solution.calcSum(l2) )
