def interval_intersection(A, B):
        
    res = []
    i = j = 0

    while i < len(A) and j < len(B):
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])

        if start <= end:
            res.append((start, end))

        if A[i][1] <= B[j][1]:
            i += 1
        else:
            j += 1


    return res