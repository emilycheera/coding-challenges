import requests

def find_tallest_starperson(int_list):
    """Using Star Wars API, find height of tallest person given list of ints."""

    height_dict = {}

    for num in int_list:

        res = requests.get(f"https://swapi.co/api/people/{num}/")

        res_json = res.json()

        height_dict[res_json["height"]] = res_json["name"]


    tallest = 0

    print(height_dict)
    for height in height_dict:

        height = int(height)

        if height > tallest:
            tallest = height


    return height_dict[str(tallest)]


print(find_tallest_starperson([1, 3, 5]))