def min_deletion_size(A):
    """Return min number of columns to delete to make every column sorted."""
        
    d_length = 0
    
    for i in range(len(A[0])):
        current_letter = ""
        for j in range(len(A)):
            if A[j][i] < current_letter:
                d_length += 1
                break
            else:
                current_letter = A[j][i]
                
    return d_length
    