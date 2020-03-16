def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served.
    
    while served_orders:
        current_served_order = served_orders.pop(0)
        
        if take_out_orders and current_served_order == take_out_orders[0]:
            take_out_orders.pop(0)
            
        elif dine_in_orders and current_served_order == dine_in_orders[0]:
            dine_in_orders.pop(0)
            
        else:
            return False
    
    if take_out_orders or dine_in_orders:
        return False
            
    return True
            

def is_first_come_first_served_better(take_out_orders, dine_in_orders, served_orders):

    # This is the same as above, with better time complexity.
    
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1
    
    for order in served_orders:
        
        if take_out_orders_index < take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1
            
        elif dine_in_orders_index < dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1
            
        else:
            return False
    
    if take_out_orders_index <= take_out_orders_max_index or dine_in_orders_index <= dine_in_orders_max_index:
        return False
            
    return True

