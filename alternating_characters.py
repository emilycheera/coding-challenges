def alternating_characters(s):

    curr_char = s[0]
    count = 0

    for i in range(1, len(s)):
        if s[i] == curr_char:
            count += 1
        else:
            curr_char = s[i]

    return count