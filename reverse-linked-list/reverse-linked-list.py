'''
Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

Author: Phil H. Cui
Date: 12/30/16
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__( self ):
        return "{}->{}".format( self.val, self.next )

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

    # dummy -> None , head = 1   ->  2   -> 3

    # dummy ->  1
    # 1 ->   None
    # head  = 2

    # dummy -> 2
    # head -> 2
    # head = 3


        # dummy = ListNode(float("-inf"))
        # while head:
        #
        #     dummy.next, head.next, head = head, dummy.next, head.next
        #
        #
        #     print dummy.next
        #     # print dummy.next
        #     print head
        #     # print head.next
        #
        # return dummy.next

        dummy = ListNode( float("-inf"))  # dummpy points to already reversed linked list

        while head:
            cur = head
            head = head.next

            cur.next = dummy.next

            dummy.next = cur

            # print dummy, head
            # equivalent to: dummy.next, head.next, head = head, dummy.next, head.next

        return dummy.next




if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)

    print Solution().reverseList(l)
