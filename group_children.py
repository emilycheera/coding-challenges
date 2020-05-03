
def group_children(ages):
    """Return minimum number of groups such that ages differ by <= 2 years."""

    ages.sort()

    left_age = ages[0]
    num_groups = 1

    for age in ages:
        if age > left_age + 2:
            left_age = age
            num_groups += 1
            
    return num_groups


print(group_children([2, 3, 6, 7, 13, 14, 15, 4]))