'''

Implement int sqrt(int x).

Compute and return the square root of x.

Author: Phil H. Cui
Date: 12/06/16

'''

class Solution(object):
    def __init__( self ):
        self.episilon = 0.001

    def mySqrt_2(self, x):
        """
        :type x: int
        :rtype: int
        """

        low, high = 0, x/2 + 1

        while low <= high:

            mid = (low + high)/2

            # if abs(mid ** 2 - x) <= self.episilon:
            #     return mid
            if mid ** 2 == x:
                return mid

            elif mid ** 2 > x:
                high = mid - 1
            else:
                low = mid + 1

        return high


    def mySqrt(self, x):

        low, high = 0, x/2 + 1

        while low <= high:
            mid = (low + high) / 2.0
            if abs(mid ** 2 - x) <= self.episilon:
                return mid
            elif mid ** 2 > x:
                high = mid
            else:
                low = mid


if __name__ == "__main__":
    x = 5
    print Solution().mySqrt( x )
