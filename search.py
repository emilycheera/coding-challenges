database = [
    {"title": "test title", "body": "test foo body"},
    {"title": "test title 2", "body": "test body"}
]


def search(term):

    found_list = []
    term_words = set(term.split(" "))

    for dictionary in database:
        title_set = set(dictionary["title"].split(" "))
        body_set = set(dictionary["body"].split(" "))

        if len(term_words - title_set) == 0 or len(term_words - body_set) == 0:
            found_list.append(dictionary)

    return found_list

assert search("test body")[0]["body"] == "test foo body"
assert search("hello") == []
assert search("test foo body")[0]["body"] == "test foo body"
