'''
There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a n x k cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color 0;
costs[1][2] is the cost of painting house 1 with color 2, and so on...
Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
Follow up:
Could you solve it in O(nk) runtime?

思路:

首先,我们来分析这个问题,假设我们遍历到第i行,我们有多少种颜色可以选择呢?
毫无疑问,是k-1种;接下来,我们来考虑这个问题,对于每一行来讲,我们肯定是都想选择cost最小的颜色,
但是题目中说了,相邻的两个房子不能涂相同的颜色,如果当前行cost最小的颜色和上一行所选择的颜色相同,
那怎么办呢?那这个颜色就不能选了,那应该选哪个呢?我们应该选择第二小的,明白了这两个问题之后,
这个题目就好做了,我们需要记录每一行cost最小的位置及cost第二小的位置,遍历过程中,并及时更新相关的值。

Author: Phil H. Cui
Date: 12/07/16
'''

class Solution( object ):
    def minCost( self, costs ):
        if not costs:
            return 0

        n, k = len(costs), len(costs[0])
        min_cost = [costs[0], [0]*k]

        for i in xrange(1,n):
            smallest, second_smallest = float('inf'), float('inf')

            # Find smallest and second_smallest for each row.
            for j in xrange(k):
                if min_cost[(i - 1) % 2][j] < smallest:
                    smallest, second_smallest = min_cost[(i - 1) % 2][j], smallest
                elif  min_cost[(i - 1) % 2][j] < second_smallest:
                    second_smallest =  min_cost[(i - 1) % 2][j]

            # Non-Smallest column for row i-1 <-> Smallest for row i;
            # Smallest column for row i-1 <-> Second smallest for row i;
            for j in xrange(k):
                min_j = smallest if min_cost[(i - 1) % 2][j] != smallest else second_smallest
                min_cost[i % 2][j] = costs[i][j] + min_j

        return min(min_cost[ (n-1) % 2 ])

if __name__ == "__main__":
    costs = [ [1,2,3], [2,2,3], [5,1,3], [3,2,3], [1,1,2] ]
    print Solution().minCost( costs )
