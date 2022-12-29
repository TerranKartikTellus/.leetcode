#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leftMost = ListNode(0,head)
        ptrL = leftMost
        ptrR = head
        
        while n>0 and ptrR:
          ptrR=ptrR.next
          n-=1

        while ptrR:
            ptrL=ptrL.next,
            ptrR=ptrR.next
        
        ptrL.next=ptrL.next.next

        return leftMost.next

# @lc code=end

