
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













