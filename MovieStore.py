from movie import movies

movie1 = movies


def autocomplete(categories, user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    # Return categories that match the user input
    suggestions = [category for category in categories if category.lower().startswith(user_input)]
    return suggestions


def get_all_genres(movie1):
    genres = set()  # Use a set to avoid duplicates
    for movie in movie1:
        for genre in movie["genre"]:
            genres.add(genre)
    return list(genres)  # Convert to list for easier processing


def get_movies_by_genre(movie1, selected_genre):
    genre_movies = [movie for movie in movie1 if selected_genre in movie["genre"]]
    return genre_movies
# Data and functions from above


def main():
    genres = get_all_genres(movie1)
    # Step 1: Autocomplete
    user_input = input("Enter the beginning of a genre: ")
    suggestions = autocomplete(genres, user_input)
    if suggestions:
        print("Suggestions:", suggestions)
        selected_genre = input("Select a genre from the suggestions: ")
        # Step 2: Retrieve Movies
        if selected_genre in suggestions:
            genre_movies = get_movies_by_genre(movies, selected_genre)
            if genre_movies:
                print(f"Movies in {selected_genre}:")
                for movie in genre_movies:
                    print(f"{movie['title']} ({movie['year']}) - Rating: {movie['rating']}")
            else:
                print(f"No movies found in {selected_genre}.")
        else:
            print("Invalid genre selected.")
    else:
        print("No suggestions found for that input.")

# Run the program


main()

# For actors:


def get_all_actors(movies):
    actors = set()
    for movie in movies:
        for actor in movie["actors"]:
            actors.add(actor)
    return list(actors)


def get_movies_by_actor(movies, selected_actor):
    actor_movies = [movie for movie in movies if selected_actor in movie["actors"]]
    return actor_movies
