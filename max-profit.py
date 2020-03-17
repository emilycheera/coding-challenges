
def get_max_profit(stock_prices):

    # Calculate the max profit in O(1) space.
    
    lowest_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    
    for price in stock_prices[1:]:
        if  price - lowest_price > max_profit:
            max_profit = price - lowest_price
        if price < lowest_price:
            lowest_price = price
    
    return max_profit
    

def get_max_profit1(stock_prices):

    # Calculate the max profit
   
    # Check if highest price is first.
    highest_price = stock_prices[0]
    highest_price_indice = 0
    for i, price in enumerate(stock_prices):
        if price > highest_price:
            highest_price = price
            highest_price_indice = i
    
    if highest_price_indice == 0:
        return stock_prices[1] - highest_price
   
    lowest_price = stock_prices[0]
    lowest_price_indice = 0
    for i, price in enumerate(stock_prices):
        if price < lowest_price:
            lowest_price = price
            lowest_price_indice = i
            
    highest_price = stock_prices[lowest_price_indice + 1]
    for price in stock_prices[lowest_price_indice + 2:]:
        if price > highest_price:
            highest_price = price
    
    return highest_price - lowest_price


