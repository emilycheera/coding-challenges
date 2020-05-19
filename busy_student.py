def busyStudent(startTime, endTime, queryTime):
    
    count = 0
    
    for start, end in zip(startTime, endTime):
        if start <= queryTime <= end:
            count += 1
    
    return count