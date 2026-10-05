# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        fast, slow = head, head
        prev_slow = None
        while fast and fast.next:
            prev_slow = slow
            fast = fast.next.next
            slow = slow.next

        if prev_slow:
            prev_slow.next = None
        
        # Reverse from slow to end
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Merge head and prev interleaving
        while head and prev:
            temp1 = head.next
            temp2 = prev.next
            head.next = prev
            if temp1:
                prev.next = temp1
            prev = temp2
            head = temp1

        
