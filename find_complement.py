def find_complement(num):
        
    # Convert num (int) to binary
    # Flip each digit in binary num
    # Convert binary num to int
    
    bin_num = bin(num)[2:]
            
    flipped_num = ""
    
    for digit in bin_num:
        if digit == "0":
            flipped_num += "1"
        else:
            flipped_num += "0"
                            
    return int(flipped_num, 2)
    