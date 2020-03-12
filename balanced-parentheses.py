def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""

    list_of_parens = []

    for char in phrase:
        if char == "(":
            list_of_parens.append("(")

        elif char == ")":
            if list_of_parens:
                list_of_parens.pop()

            else:
                return False

    if list_of_parens:
        return False

    return True