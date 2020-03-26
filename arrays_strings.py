
def is_unique(string):
    """Determine if a string has all unique characters."""

    # Assuming character set is ASCII
    if len(string) > 128:
        return False

    str_len = len(string)
    str_set = set(string)

    if str_len != len(str_set):
        return False
    return True

print("test 'hihi' -> False")
print(is_unique("hihi"))
print("test 'abcde' -> True")
print(is_unique("abcde"))



def check_permutation(str1, str2):
    """Determine if one string is a permuation of the other."""

    if len(str1) != len(str2):
        return False

    char_dict  = {}

    for char in str1:
        char_dict[char] = char_dict.get(char, 0) + 1

    for char in str2:
        if char_dict.get(char) == None:
            return False
        char_dict[char] -= 1

    return True

print("test 'abcbcd', 'dcabbc' -> True")
print(check_permutation("abcbcd", "dcabbc"))
print("test 'sofa', 'soft' -> False")
print(check_permutation("sofa", "soft"))



def URLify(string):
    """Replace all spaces in a string with '%20' and remove trailing spaces."""

    last_index_with_char = 0

    for i in range(1, len(string)):
        if string[i] != " ":
            last_index_with_char = i

    strip_str = string[0:last_index_with_char + 1]

    return "%20".join(strip_str.split(" "))

print("test 'hello beautiful world       ' -> 'hello%20beautiful%20world'")
print(URLify("hello beautiful world       "))
print("test 'hello   ' -> 'hello'")
print(URLify("hello   "))



def palindrome_permutation(string):
    """Check if the string is a permutation of a palindrome."""

    char_counts = {}

    for char in string:
        if char == " ":
            continue
        char = char.lower()
        char_counts[char] = char_counts.get(char, 0) + 1

    odd_count = 0

    for count in char_counts.values():
        if count % 2 == 1:
            if len("".join(string.split(" "))) % 2 == 0:
                return False
            if odd_count > 0:
                return False
            odd_count += 1

    return True

print("test 'Tact Coa' -> True")
print(palindrome_permutation("Tact Coa"))



def one_away(string1, string2):
    """Check if the strings are one or less edits away."""

    char_counts = {}

    for char in string1:
        char_counts[char] = char_counts.get(char, 0) + 1

    count_different = False

    for char in string2:
        if char_counts.get(char) == None:
            if count_different == True:
                return False
            count_different = True
        else:
            if char_counts.get(char) == 1:
                del char_counts[char]
            else:
                char_counts.get(char) -+ 1

    if count_different == False:
        if len(char_counts) > 1:
            return False

    return True

def one_away2(string1, string2):
    """Check if the strings are one or less edits away."""

    if len(string1) == len(string2):
        return check_replace(string1, string2)
    elif len(string1) - len(string2) == 1:
        return check_insert_or_removal(string1, string2)
    elif len(string1) - len(string2) == -1:
        return check_insert_or_removal(string2, string1)
    else:
        return False

def check_replace(string1, string2):
    """Check if the strings have only one letter different."""

    count_different = False

    for (s1, s2) in zip(string1, string2):
        if s1 != s2:
            if count_different == True:
                return False
            count_different = True

    return True

def check_insert_or_removal(string1, string2):
    """Check that strings are equal except one insert or removal."""

    i, j = 0, 0
    edited = False

    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if edited:
                return False
            edited == True
            i += 1
        else:
            i += 1
            j += 1

    return True

print("test 'pale', 'ple' -> True")
print(one_away2("pale", "ple"))
print("test 'pales', 'pale' -> True")
print(one_away2("pales", "pale"))
print("test 'pale', 'bale' -> True")
print(one_away2("pale", "bale"))
print("test 'pale', 'bake' -> False")
print(one_away2("pale", "bake"))



def string_compression(string):
    """Compress a string using counts of repeated characters."""

    letter = string[0]
    letter_count = 0
    compressed_list = []

    for char in string:
        if char == letter:
            letter_count += 1
        else:
            compressed_list.append(f"{letter}{letter_count}")
            letter = char
            letter_count = 1

    compressed_list.append(f"{letter}{letter_count}")

    return min("".join(compressed_list), string, key=len)

print("test 'aabcccccaaa' -> 'a2b1c5a3'")
print(string_compression("aabcccccaaa"))
print("test 'abcde' -> 'abcde'")
print(string_compression("abcde"))



def rotate_matrix(matrix):
    """Rotate NxN matrix by 90 degrees."""

    length = len(matrix)
    layers = length // 2

    for i in range(layers):
        for j in range(i, length - 1 - i):

            # Save top
            top = matrix[i][j]

            # Top = Left
            matrix[i][j] = matrix[length - 1 - j][i]

            # Left = Bottom
            matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]

            # Bottom = Right
            matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]

            # Right = Top
            matrix[j][length - 1 - i] = top

    return matrix

# Tests    
orig_matrix = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
rotated_matrix = [[21, 16, 11, 6, 1],
                  [22, 17, 12, 7, 2],
                  [23, 18, 13, 8, 3],
                  [24, 19, 14, 9, 4],
                  [25, 20, 15, 10, 5]]
print(f"test {orig_matrix} -> {rotated_matrix}")
print(rotate_matrix(orig_matrix))
print("************")



def zero_matrix(matrix):
    """If a matrix element is 0, set its entire row and column to 0."""

    zero_coords = []
    nrows = range(len(matrix))
    ncols = range(len(matrix[0]))

    for i in nrows:
        for j in ncols:
            if matrix[i][j] == 0:
                zero_coords.append((i, j))

    for row, col in zero_coords:
        for i in ncols:
            matrix[row][i] = 0
        for j in nrows:
            matrix[j][col] = 0

    return matrix

# Tests
orig_matrix = [[1,  2,  0,  4,  5],
               [6,  7,  8,  9,  10],
               [11, 12, 13, 14, 15],
               [16, 0,  18, 19, 20],
               [21, 22, 23, 24, 25]]
zerod_matrix = [[0,  0, 0, 0,  0],
               [6,  0, 0, 9,  10],
               [11, 0, 0, 14, 15],
               [0,  0, 0, 0,  0],
               [21, 0, 0, 24, 25]]

print(f"test {orig_matrix} -> {zerod_matrix}")
print(zero_matrix(orig_matrix))



def is_substring(string, sub):
    return sub in string


def string_rotation(s1, s2):
    """Check if s2 is a rotation of s1 making a call to is_substring once."""
    return is_substring(s1+s1, s2)

print("test 'waterbottle', 'erbottlewat' -> True")
print(string_rotation("waterbottle", "erbottlewat"))
print("test 'hello', 'helloo' -> False")
print(string_rotation("hello", "helloo"))




