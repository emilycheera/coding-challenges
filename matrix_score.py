def matrix_score(A):
        
    # Loop through each row, if leftmost digit is 0, toggle that row
    for row in A:
        if row[0] == 0:
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
    
    # Loop through columns starting at pos 1, toggle col if count 0 > count 1
    for i in range(1, len(A[0])):
        col_counts = []
        for j in range(len(A)):
            col_counts.append(A[j][i])
        if col_counts.count(0) > col_counts.count(1):
            for j in range(len(A)):
                if A[j][i] == 0:
                    A[j][i] = 1
                else:
                    A[j][i] = 0
    
    
    # Get score of final matrix
    final_score = 0
    
    for row in A:
        current_bin = ""
        for num in row:
            current_bin += str(num)
            
        final_score += int(current_bin, 2)
        
    return final_score
    