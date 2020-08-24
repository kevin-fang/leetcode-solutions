# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        
        after = self.swapPairs(head.next.next)
        tmp = head.next
        head.next = after
        tmp.next = head
        return tmp
