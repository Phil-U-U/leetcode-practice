'''
Reverse the second half of a singly linked list.

Hint:
Use two pointers, a fast one that runs twice the speed of the slow one;
In that way, the slow one will reach the middle when the fast one reaches the end. 


Author: Phil H. Cui
Date: 01/02/16
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__( self ):
        return "{}->{}".format( self.val, self.next )



class Solution(object):

	def reverseLinkedList( self, head):
		dummy = ListNode( float( "-inf") )

		while head:
			dummy.next, head.next, head = head, dummy.next, head.next

		return dummy.next	

	def reverseSecondHalfList( self, head ):      

		if head is None or head.next is None:
			return head

		dummy = ListNode( float("-inf") )	  
		dummy.next = head

		fast, slow = dummy, dummy

		while fast.next is not None and fast.next.next is not None:
			fast, slow = fast.next.next, slow.next

		slow.next = self.reverseLinkedList( slow.next )	

		return dummy.next



if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    # 1 -> 2 -> 3 -> 4 -> None
    print l
    print Solution().reverseSecondHalfList(l)
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    print l
    print Solution().reverseSecondHalfList(l)