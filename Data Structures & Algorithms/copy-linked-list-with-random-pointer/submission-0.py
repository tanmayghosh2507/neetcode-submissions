"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        rand_map = {} # index -> (Node, new Node)
        dummy = head
        new_head = copy_dummy = Node(-1)

        while dummy:
            copy_dummy.next = Node(dummy.val)
            copy_dummy = copy_dummy.next
            rand_map[dummy] = copy_dummy
            dummy = dummy.next
            
        while head:
            rand = head.random
            if rand is not None:
                rand_map[head].random = rand_map[rand]
            head = head.next

        return new_head.next
        
