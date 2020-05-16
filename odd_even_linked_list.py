"""Given a singly linked list, group all odd nodes together followed by the 
   even nodes. The program should run in O(1) space and O(n) time."""

def odd_even_linked_list(head):
        
    if not head:
        return head
    
    current = head
    evens_head = current.next
    evens = current.next
    
    while current and evens and current.next and evens.next:
        
        current.next = evens.next
        current = current.next
        evens.next = current.next
        evens = evens.next
    
    current.next = evens_head
    
    return head