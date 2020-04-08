def find_middle_node(head):

    fast_node = head
    slow_node = head
    
    while fast_node and fast_node.next:
        fast_node = fast_node.next.next
        slow_node = slow_node.next
    
    return slow_node