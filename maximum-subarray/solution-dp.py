'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

Author: Phil H. Cui
Date: 11/29/16
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max = nums[0]
        global_max = local_max

        for cur in nums[1:]:
            local_max = max( cur, cur+local_max )  # boarder can't be negative, include former elements or not
            global_max = max( local_max, global_max ) # DP, record maximum till now, because this step, I can look into the                                           # future fearlessly

        return global_max
