
'''
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs0 is the cost of painting house 0 with color red; costs1 is the cost of painting house 1 with color green, and so on...
Find the minimum cost to paint all houses.

Note: All costs are positive integers.


直到房子i，其最小的涂色开销是直到房子i-1的最小涂色开销，加上房子i本身的涂色开销。
但是房子i的涂色方式需要根据房子i-1的涂色方式来确定，所以我们对房子i-1要记录涂三种颜色分别不同的开销，
这样房子i在涂色的时候，我们就知道三种颜色各自的最小开销是多少了。我们在原数组上修改，可以做到不用空间。



Author: Phil H. Cui
Date: 12/07/16

'''
class Solution(object):
    def min_cost( self, costs ):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # DP
        if not costs:
            return 0

        n = len(costs)

        for i in xrange(1,n):

            costs[i][0] += min( costs[i-1][1], costs[i-1][2] )
            costs[i][1] += min( costs[i-1][0], costs[i-1][2] )
            costs[i][2] += min( costs[i-1][0], costs[i-1][1] )

        return min(costs[n-1])




class Solution2(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        min_cost = [costs[0], [0, 0, 0]]

        n = len(costs)
        for i in xrange(1, n):
            min_cost[i % 2][0] = costs[i][0] + \
                                 min(min_cost[(i - 1) % 2][1], min_cost[(i - 1) % 2][2])
            min_cost[i % 2][1] = costs[i][1] + \
                                 min(min_cost[(i - 1) % 2][0], min_cost[(i - 1) % 2][2])
            min_cost[i % 2][2] = costs[i][2] + \
                                 min(min_cost[(i - 1) % 2][0], min_cost[(i - 1) % 2][1])

        return min(min_cost[(n - 1) % 2])


if __name__ == "__main__":
    costs = [ [1,2,3], [2,2,3], [5,1,3], [3,2,3], [1,1,2] ]
    print Solution().min_cost( costs )
    # print Solution2().minCost( costs )
    # print Solution3().minCost( costs )
