'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Author: Phil H. Cui
Date: 12/02/16

[2,3]
[3,2]

'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Divide and Conquer, Recursion
        res = []

        if len(nums) == 1:

            return [nums]

        for i, num in enumerate(nums):

            rest = nums[:i] + nums[i+1:]

            for restPermutation in self.permute( rest ):
                # print restPermutation will see why return [nums]: for loop get an element from list, list of list
                res.append( [nums[i]] + restPermutation )

        return res

if __name__ == '__main__':
    nums = [1,2,3]
    print Solution().permute( nums )
