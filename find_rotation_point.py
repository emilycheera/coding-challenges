def find_rotation_point(words):
    """Find the rotation point in the list."""
    
    floor = -1
    ceiling = len(words)
    
    while floor < ceiling:
        mid = (ceiling - floor) // 2 + floor
        if words[mid - 1] > words[mid]:
            return mid
        if words[mid] < words[0]:
            ceiling = mid
        else:
            floor = mid
