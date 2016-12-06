'''
Implement pow(x, n).

Author: Phil H. Cui
Date: 12/06/16
'''





class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        elif n < 0:
            return 1.0 / self.myPow( x, -n )
        else: # n > 0:
            if n % 2 == 0:  # even
                return self.myPow( x*x, n/2 ) # return self.myPow( x, n/2 ) **2  # 
            else: # n % 2 != 0   # odd
                return x * self.myPow( x, n-1 )


if __name__ == "__main__":
    x, n = 2, -5
    print Solution().myPow( x, n )
