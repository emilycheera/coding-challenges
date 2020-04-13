"""Calculator

    >>> calc("+ 1 2")  # 1 + 2
    3

    >>> calc("* 2 + 1 2")  # 2 * (1 + 2)
    6

    >>> calc("+ 9 * 2 3")   # 9 + (2 * 3)
    15

Let's make sure we have non-commutative operators working:

    >>> calc("- 1 2")  # 1 - 2
    -1

    >>> calc("- 9 * 2 3")  # 9 - (2 * 3)
    3

    >>> calc("/ 6 - 4 2")  # 6 / (4 - 2)
    3
"""


def calc(s):
    """Evaluate expression."""

    tokens = s.split(" ")

    nums = []
    operators = []

    for token in tokens:
        if token.isnumeric():
            nums.append(int(token))
        else:
            operators.append(token)

    num2 = nums.pop()

    while operators:
        num1 = nums.pop()
        operator = operators.pop()

        if operator == "+":
            num2 = num1 + num2
        elif operator == "-":
            num2 = num1 - num2
        elif operator == "*":
            num2 = num1 * num2
        else:
            num2 = num1 // num2

    return num2









if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; WELL-CALCULATED! ***\n")
