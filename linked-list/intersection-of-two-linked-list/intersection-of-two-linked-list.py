# Time:  O(m + n)
# Space: O(1)
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 - a2
#                    \
#                      c1 - c2 - c3
#                    /
# B:     b1 - b2 - b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#

# Definition for singly-linked list.
class ListNode(object):
    def __init__( self, x ):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{} -> {}".format( self.val, self.next)

class Solution( object ):
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode( self, headA, headB ):
        if not headA or not headB:
            return None

        lookup = set()
        curA, curB = headA, headB
        merge = None

        while curA:
            lookup.add( curA )
            curA = curA.next

        # print curB.next.next.next in lookup

        while curB:
            if curB in lookup:
                merge = curB
                break
            else:
                curB = curB.next

        return merge

    def getIntersectionNode_2( self, headA, headB ):
        # 双指针循环
        if not headA or not headB:
            return None

        curA, curB = headA, headB
        merge, tailA, tailB = None, None, None

        while curA and curB:
            if curA == curB:
                merge = curA
                break

            if curA.next:
                curA = curA.next
            elif tailA is None:
                tailA = curA
                curA = headB
            else:
                break

            if curB.next:
                curB = curB.next
            elif tailB is None:
                tailB = curB
                curB = headA
            else:
                break

        return merge

if __name__ == "__main__":
    headA = ListNode('a1')
    headA.next = ListNode('a2')
    headA.next.next = ListNode('c1')
    headA.next.next.next = ListNode('c2')
    headA.next.next.next.next = ListNode('c3')

    headB = ListNode('b1')
    headB.next = ListNode('b2')
    headB.next.next = ListNode('b3')
    headB.next.next.next = headA.next.next

    print headA
    print headB


    print Solution().getIntersectionNode_2( headA, headB )
