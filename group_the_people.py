"""There are n people whose IDs go from 0 to n - 1 and each person belongs 
exactly to one group. Given the array groupSizes of length n telling the group 
size each person belongs to, return the groups there are and the people's IDs 
each group includes.

You can return any solution in any order and the same applies for IDs. 
Also, it is guaranteed that there exists at least one solution. """

def groupThePeople(group_sizes):
        
    groups = []
            
    for i, size in enumerate(group_sizes):
        if size == 0:
            continue
        current_group = [i]
        group_sizes[i] = 0

        for j in range(i + 1, len(group_sizes)):
            if len(current_group) == size:
                break
            if group_sizes[j] == size:
                current_group.append(j)
                group_sizes[j] = 0
        
        groups.append(current_group)
        
        
    return groups