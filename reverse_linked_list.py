"""Reverses a linked list both recursively and iteratively"""
class Node():
    """Building blocks of a linked list"""

    def __init__(self, e):
        """creates a new node with element e as the value"""
        self.val = e
        self.next = None

class Solution():
    
    def iter_reverse(self, head: ListNode) -> ListNode:
        """Returns a linked list reversed"""
        tail = None
        while head:
            tmp = head.next
            head.next = tail
            tail = head
            head = tmp
        return tail
