def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    while num > 0:
        digit = num % 10
        print(digit)

        num -= digit
        num //= 10
