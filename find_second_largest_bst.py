def find_second_largest(root_node):

    # Find the second largest item in the binary search tree
    
    if root_node is None or (root_node.left is None and root_node.right is None):
        raise ValueError('Tree must have at least 2 nodes.')
    
    max_nums = []
    
    to_visit = [root_node]
    
    while to_visit:
        node = to_visit.pop()
        
        if not max_nums:
            max_nums.append(node.value)
            
        elif len(max_nums) == 1:
            if max_nums[0] > node.value:
                max_nums.append(node.value)
            else:
                max_nums.insert(0, node.value)
            
        elif node.value > max_nums[0]:
            max_nums[0], max_nums[1] = node.value, max_nums[0]
            
        elif max_nums[0] > node.value > max_nums[1]:
            max_nums[1] = node.value
            
        if node.right:
            to_visit.append(node.right)
            
        if not node.right and node.left:
            to_visit.append(node.left)
            
    return max_nums[1]
        