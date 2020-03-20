import random


def shuffle(the_list):

    # Shuffle the input.

    new_list = [None for i in range(len(the_list))]
    index = random.randrange(0, len(the_list))

    for item in the_list:
        while new_list[index]:
            index = random.randrange(0, len(the_list))
        
        new_list[index] = item

    return new_list


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling)


def shuffle_in_place(the_list):

    # Same as above, except shuffle the input in place.
    
    if len(the_list) == 1:
        return the_list
        
    for index_to_update in range(0, len(the_list) - 1):
        random_index = get_random(index_to_update, len(the_list) - 1)
        the_list[index_to_update], the_list[random_index] = \
            the_list[random_index], the_list[index_to_update] 
    
    
    return the_list