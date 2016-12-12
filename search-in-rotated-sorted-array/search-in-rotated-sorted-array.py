'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Author: Phil H. Cui
Date: 12/01/16

'''

class Solution(object):
    def search(self, A, target):
        low, high = 0, len(A)

        while low < high:
            mid = low + (high - low) / 2

            if A[mid] == target:
                return mid

            if A[low] <= A[mid]: # Left half is sorted
                if A[low] <= target and target < A[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:               # Right half is sorted
                if A[mid] < target and target <= A[high - 1]:
                    low = mid + 1
                else:
                    high = mid

        return -1

    def search_Phil(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        isFound = False
        i, cnt = 0, 0
        while (not isFound) and (cnt < len(nums)):
            if target == nums[i]:
                isFound = True
                if i < 0:
                    return i+len(nums)
                else:
                    return i

            elif target > nums[i]:
                i += 1

            elif target < nums[i]:
                i -= 1

            cnt += 1

        return -1
