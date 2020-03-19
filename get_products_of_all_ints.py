
def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products.
    
    if len(int_list) < 2:
        raise Exception

    final_list = []

    for i in range(len(int_list)):
        product = 1
        for j in range(len(int_list)):
            if i == j:
                continue
            else:
                product *= int_list[j]
       
        final_list.append(product)
        
    return final_list
