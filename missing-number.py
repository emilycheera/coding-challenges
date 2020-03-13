# Imagine a list of numbers from 1 to max_num, inclusive – except that one 
# of these numbers will be missing from the list.

# You should write a function that takes this list of numbers, as well as 
# the max_num, and it should return the missing number.

def missing_number(num_list, max_num):
    """Find the missing number in the list.
    
    For example, in a randomed order list of 1-10, 8 was removed.
    This function should return 8.

    >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
    8

    """

    range_set = set(range(1, (max_num + 1)))

    num_list_set = set(num_list)

    missing_number = range_set - num_list_set

    return missing_number.pop()


def missing_number_faster(num_list, max_num):
    """Find the missing number in O(n log n) time."""

    num_list.sort()

    current_num = 1

    for num in num_list:
        if num != current_num:
            return num - 1
        current_num += 1


