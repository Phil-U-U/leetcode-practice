'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

VS

[1,2,3] ->
[
    [1,2,3],  [1,2,1]
    [1,3,2],  [1,1,2]
    [2,1,3],  [2,1,1]
    [2,3,1],  [2,1,1]
    [3,1,2],  [1,1,2]
    [3,2,1],  [1,2,1]
]

Author: Phil H. Cui
Date: 12/02/16
'''



class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            return [nums]

        res = []
        duplicates = set()

        for i, num in enumerate(nums):
            if num in duplicates:
                continue
            else:
                duplicates.add( num )

                rest = nums[:i] + nums[i+1:]

                for restPermutation in self.permuteUnique( rest ):
                    res.append( [num] + restPermutation )

        return res

if __name__ == '__main__':
    nums = [1, 2, 1]
    print Solution().permuteUnique( nums )
