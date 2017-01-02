'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

Author: Phil H. Cui
Date: 12/31/16

'''

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}

        for i, number in enumerate(numbers, 1):
            if number*target >0 and number > target:
                return False

            if number not in lookup:
                lookup[target - number] = i
            else:
                return lookup[number], i


    def twoSum_2(self, nums, target):
        start, end = 0, len(nums) - 1

        while start != end:
            sum = nums[start] + nums[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]

if __name__ == "__main__":
    numbers, target = [2, 7, 11, 15], 9
    print Solution().twoSum( numbers, target )

    numbers, target = [-3, 3, 4, 90], 0
    print Solution().twoSum( numbers, target )
