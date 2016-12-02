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

'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # DFS, Queue
        res = []
        queue = []

        while( queue ):
            node = queue.pop(0)
            




if __name__ == '__main__':
    nums = [1,2,3]
    print Solution().permute( nums )
