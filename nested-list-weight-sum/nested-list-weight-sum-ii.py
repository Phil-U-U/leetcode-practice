'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:
Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)

Author: Phil H. Cui
Date: 12/02/16
'''
class Solution( object ):
    def calcSum( self, NestedList, Unweighted = 0, Weighted = 0 ):

        if len(NestedList) == 0:
            return Weighted

        NextLevel = []

        for x in NestedList:
            if type(x) == int:
                Unweighted += x
            elif type(x) == list:
                for y in x:
                    NextLevel.append(y)

        Weighted += Unweighted

        return self.calcSum(NextLevel, Unweighted, Weighted )


if __name__ == "__main__":
    l1 = [[1,1],2,[1,1]]
    l2 = [1,[4,[6]]]
    l3 = [ [[[1,1]]], 2, [1,1]]
    l4 = [ [[1,1]] ]
    solution = Solution()
    print "{}-{}".format(8, solution.calcSum(l1) )
    print "{}-{}".format(17, solution.calcSum(l2) )
    print "{}-{}".format(12, solution.calcSum(l3) )
    print solution.calcSum(l4)
