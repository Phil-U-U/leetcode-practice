#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Time:  O(nlogk)
Space: O(k)
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

将每个list的最小节点放入一个priority queue (min heap)中。
之后每从queue中取出一个节点，则将该节点在其list中的下一个节点插入，
以此类推直到全部节点都经过priority queue。由于priority queue的大小为始终为k，
而每次插入的复杂度是log k，一共插入过n个节点。时间复杂度为O(nlogk)，
空间复杂度为O(k)。

Author: Phil H. Cui
Date: 01/02/2017
'''

from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode( float('-inf') )
        cur = dummy

        heap = []

        for list in lists:  # list has been sorted
        	heappush( heap, (list.val, list) )


        while heap:

        	smallest = heappop( heap )[1]

        	cur.next = smallest
        	cur = cur.next

        	left = smallest.next
        	if left:
        		heappush( heap, (left.val, left) )



        return dummy.next

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list2 = ListNode(2)
    list2.next = ListNode(4)
    
    print Solution().mergeKLists([list1, list2])
