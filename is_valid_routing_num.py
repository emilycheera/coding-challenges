def is_routing_number(num):

    digits = []

    while num > 0:
        digits.append(num % 10)
        num //= 10

    digits.reverse()

    if len(digits) != 9:
        return False

    routing_sum = (3 * (digits[0] + digits[3] + digits[6])) + (
        7 * (digits[1] + digits[4] + digits[7]) + digits[2] + digits[5] + digits[8]
    )

    return routing_sum % 10 == 0
