def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    
    sorted_list = []
    
    while my_list or alices_list:
        if not my_list:
            sorted_list.extend(alices_list)
            break
        elif not alices_list:
            sorted_list.extend(my_list)
            break
        elif my_list[0] < alices_list[0]:
            sorted_list.append(my_list.pop(0))
        else:
            sorted_list.append(alices_list.pop(0))

    return sorted_list