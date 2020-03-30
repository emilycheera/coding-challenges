def is_binary_search_tree(root):

    # Determine if the tree is a valid binary search tree

    node_and_bounds_stack = [(root, float('inf'), -float('inf'))]
    
    while node_and_bounds_stack:
        node, upper_bound, lower_bound = node_and_bounds_stack.pop()
        
        if (node.value >= upper_bound) or (node.value <= lower_bound):
            return False
            
        if node.left:
            node_and_bounds_stack.append((node.left, node.value, lower_bound))
        
        if node.right:
            node_and_bounds_stack.append((node.right, upper_bound, node.value))
            
    return True