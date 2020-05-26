def get_target_copy(cloned, target):
        
    to_visit = [cloned]
    
    while to_visit:
        current = to_visit.pop()
        if current.val == target.val:
            return current
        if current.left:
            to_visit.append(current.left)
        if current.right:
            to_visit.append(current.right)
        