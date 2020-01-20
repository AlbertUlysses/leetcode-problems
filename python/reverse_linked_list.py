class Solution:
    
    def iter_reverse(self, head: ListNode) -> ListNode:
        """Returns a linked list reversed"""
        tail = None #set tail to None
        while head: #Traverses through the linked list
            temp = head.next #assign the temp variable to the value after the head 
            head.next = tail #reassign the next value to the tail
            tail = head #reassigns the tail to head 
            head = tmp #reassigns head to the next value of the list until it's None
        return tail #returns the new reversed linked list


