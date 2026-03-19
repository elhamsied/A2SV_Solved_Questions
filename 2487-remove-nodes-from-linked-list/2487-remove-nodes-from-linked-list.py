# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head):
        
        # reverse the list
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        head = reverse(head)
        
        max_val = 0
        curr = head
        prev = None
        
        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                prev = curr
            else:
                prev.next = curr.next  
            curr = curr.next
        
        return reverse(head)