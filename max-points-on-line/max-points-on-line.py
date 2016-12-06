
'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Solution:
To find the maximum number of points lying on the same line,
First, form all possible lines: n choose 2 lines in total. So at most an embeded for loops is needed for an enumeration of n(n-1)/2.
During the enumeration of each line, check if the rest of points lie on the line.
No need to go back and check those already checked, since AB-C, BC-A share the same relationship.
Details: pay attention to
    (1) overlap points
    (2) Slope == inf

Author: Phil H. Cui
Date: 12/06/16

'''

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        max_points = 0
        for i, start in enumerate( points ):
            lookup = {} # key is slope, value is the number of points have the same slope
            same_points = 1

            for end in points[i+1:]:

                # start and end are the same
                if start.x == end.x and start.y == end.y:
                    same_points += 1
                else:
                    if start.x == end.x:
                        slope = float("inf")
                    else:
                        slope = 1.0 * ( end.y - start.y ) / ( end.x - start.x )


                    if slope not in lookup:
                        lookup[slope] = 1
                    else:
                        lookup[slope] += 1

                    print slope

            current_max = same_points
            for slope in lookup:
                current_max = max( current_max, lookup[slope] + same_points )

            max_points = max( max_points, current_max )

        return max_points




if __name__ == "__main__":
    points = [Point(1,2), Point(1,3), Point(2,1)]
    print Solution().maxPoints( points )
