def hourglass_sum(arr):
    
    hourglass_values = []

    for i in range(len(arr) - 2):
        for j in range(len(arr[0]) - 2):
            current_value= 0
            for k in range(3):
                current_value += arr[j][i + k]
            current_value += arr[j + 1] [i + 1]
            for k in range(3):
                current_value += arr[j + 2][i + k]

            hourglass_values.append(current_value)

    return max(hourglass_values)

