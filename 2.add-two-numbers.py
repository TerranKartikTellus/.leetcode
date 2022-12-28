#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode(0)
        ptr = newNode
        carry,digit = 0,0

        while( l1 or l2 or carry ):
            if l1: 
                digit+=l1.val
                l1=l1.next
            if l2: 
                digit+=l2.val
                l2=l2.next
            if carry: digit+=carry
            
            carry = digit//10
            digit = digit%10

            ptr.next = ListNode(digit)
            ptr = ptr.next
            digit=0
            
            
        
        return newNode.next


# @lc code=end

