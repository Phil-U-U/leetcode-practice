'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Author: Phil H. Cui
Date: 12/01/16

'''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        cur = nums[0]
        res, curMin, curMax = cur, cur, cur

        if len(nums) < 2:
            return cur
        else:
            for x in nums[1:]:
                curMin_cp = curMin
                curMin = min( x, min( x*curMin, x*curMax ) )
                curMax = max( x, max( x*curMin_cp, x*curMax ) )

                res = max( curMax, res )

        return res


if __name__ == '__main__':
    nums = [2,3,-2,4]
    print '{}-{}'.format( 6, Solution().maxProduct( nums ) )
