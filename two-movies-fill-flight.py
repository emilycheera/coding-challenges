
def can_two_movies_fill_flight_1(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    
    for i, movie1 in enumerate(movie_lengths):
        for j, movie2 in enumerate(movie_lengths):
            if i != j and movie1 + movie2 == flight_length:
                return True

    return False


def can_two_movies_fill_flight_2(movie_lengths, flight_length):

    # This is the same as above, but in O(n) time using a set.
    
    movie_set = set()
    
    for movie in movie_lengths:
        if (flight_length - movie) in movie_set:
            return True
            
        movie_set.add(movie)

    return False