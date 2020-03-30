

def combine_sort(lst1, lst2):

    new_list = []

    while lst1 and lst2:
        if lst1[0] <= lst2[0]:
            new_list.append(lst1.pop(0))

        else:
            new_list.append(lst2.pop(0))

    while lst1:
        new_list.append(lst1.pop(0))

    while lst2:
        new_list.append(lst2.pop(0))

    return new_list


def merge_sort(lst):
    
    if len(lst) < 2:
        return lst

    left_side = lst[:len(lst) // 2]
    right_side = lst[len(lst) // 2:]

    lst1 = merge_sort(left_side)
    lst2 = merge_sort(right_side)

    return combine_sort(lst1, lst2)

