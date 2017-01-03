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
    def reverseList_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode( float("-inf"))  # dummpy points to already reversed linked list

        while head:
            cur = head
            head = head.next

            cur.next = dummy.next

            dummy.next = cur

            # print dummy, head
            # equivalent to: dummy.next, head.next, head = head, dummy.next, head.next

        return dummy.next


    def reverseList( self, head ):
        # dummy points to reversed list
        # head leads the node that haven't been reversed
        # read one node a time and put it to the reversed linked list
        # （1）dummy 指向刚摘下来／新读进来的node， （2）这个node被修改指向dummy原来指向的node
        # head 往后挪动一位

        # 1 -> 2 -> 3 -> None

        # dummy -> None
        # head = 1 -> 2 -> 3 -> None

        # dummy -> 1  # dummy.next = head: dummy points to the node that just being picked up from original list
        # 1 -> None (Now: dummy -> 1 -> None)  # head.next = dummy.next, here dummy is from last loop)
        # head = 2 -> 3  # head = head.next 
        
        # dummy -> 2   
        # 2 -> 1 -> None  ( dummy -> 2 -> 1 -> None )
        # head = 3 -> None
        

        # dummy -> 3
        # 3 -> 2 -> 1 -> None
        # head = None
        # Now: dummy -> 3 -> 2 -> 1 -> None
        

        dummy = ListNode( float("-inf") )   

        while head:

            dummy.next, head.next, head = head, dummy.next, head.next

        return dummy.next




if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)

    print Solution().reverseList(l)
