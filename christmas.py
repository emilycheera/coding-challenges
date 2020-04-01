from random import randint

people = ["harry", "john", "joan", "john", "bill", "john", "emily", "jill", 
          "jacob", "roy"]

last_years_matches = {0:1, 1:0, 2:3, 3:2, 4:5, 5:4, 6:7, 7:6, 8:9, 9:8}

def match_secret_santas(people, last_years_matches):

    new_matches = {}

    for i in range(len(people)):
        if i in new_matches:
            continue
        
        rand_match = randint(i + 1, len(people) - 1)

        while rand_match in new_matches:
            rand_match = randint(i + 1, len(people) - 1)

        new_matches[i] = rand_match
        new_matches[rand_match] = i

    return new_matches



print(match_secret_santas(people, last_years_matches))
